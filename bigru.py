
import re
from tensorflow.python.keras.layers import Input, GRU, Dense, Concatenate, TimeDistributed, Bidirectional, LSTM, AdditiveAttention, Attention
from tensorflow.python.keras.models import Model
import numpy as np
from sklearn.model_selection import train_test_split
import threading
from multiprocessing import Pool
from multiprocessing import freeze_support
import keras
import multiprocessing
import time
import tensorflow as tf
import os
from tensorflow.python.keras.layers import Layer
from tensorflow.python.keras import backend as K



batch_size = 64  # Batch size for training.
epochs = 20  # Number of epochs to train for.
latent_dim = 512  # Latent dimensionality of the encoding space.
learning_rate = 0.001
train_dataset_file = "combdataset1.txt"
lexicon_file = "sanlexicon.txt"
lookupfile = 'result/sanbigru_A.txt'
#
## change the name of the model to be saved
modelsavename = "modelweights"

#mode = "train" or mode = "test"
mode = "test"

input_texts = []

target_texts = []
characters = set()


with open(train_dataset_file) as fp:
    tests = fp.read().splitlines()
for x in tests:
    x = x.split('\t')
    if len(x[0])>20:
        continue
    input_texts.append(x[0])
    x[1] = '&' + x[1] + '$'
    target_texts.append(x[1])
    for char in x[0]:
        if char not in characters:
            characters.add(char)
    for char in x[1]:
        if char not in characters:
            characters.add(char)

input_texts, X_tests, target_texts, Y_tests = train_test_split(input_texts, target_texts, test_size=0.01, random_state=1)


characters.add('क्ष') 
characters.add('ळ')
characters.add('*')

characters = sorted(list(characters))
num_tokens = len(characters)
max_encoder_seq_length = max([len(txt) for txt in input_texts])
max_decoder_seq_length = max([len(txt) for txt in target_texts])

print('Number of samples:', len(input_texts))
print('Number of unique tokens:', num_tokens)
print('Max sequence length for inputs:', max_encoder_seq_length)
print('Max sequence length for outputs:', max_decoder_seq_length)




token_index = dict([(char, i) for i, char in enumerate(characters)])

encoder_input_data = np.zeros((len(input_texts), max_encoder_seq_length, num_tokens), dtype='float32')
decoder_input_data = np.zeros((len(input_texts), max_decoder_seq_length, num_tokens), dtype='float32')
decoder_target_data = np.zeros((len(input_texts), max_decoder_seq_length, num_tokens), dtype='float32')

for i, (input_text, target_text) in enumerate(zip(input_texts, target_texts)):
    for t, char in enumerate(input_text):
        encoder_input_data[i, t, token_index[char]] = 1.
    encoder_input_data[i, t + 1:, token_index['*']] = 1.
    for t, char in enumerate(target_text):
        # decoder_target_data is ahead of decoder_input_data by one timestep
        decoder_input_data[i, t, token_index[char]] = 1.
        if t > 0:
            # decoder_target_data will be ahead by one timestep
            # and will not include the start character.
            decoder_target_data[i, t - 1, token_index[char]] = 1.
    decoder_input_data[i, t + 1:, token_index['*']] = 1.
    decoder_target_data[i, t:, token_index['*']] = 1.

#dropout
dp = 0.2
encoder_inputs = Input(shape=(None, num_tokens))
encoder = Bidirectional(GRU(latent_dim, return_state=True, dropout=dp))
encoder_outputs, state_h, state_c = encoder(encoder_inputs)
final_state = Concatenate()([state_h, state_c])

decoder_inputs = Input(shape=(None, num_tokens))

# We set up our decoder to return full output sequences,
# and to return internal states as well. We don't use the
# return states in the training model, but we will use them in inference.
decoder_gru = GRU(latent_dim*2, return_sequences=True, return_state=True, dropout=dp)
decoder_outputs, _ = decoder_gru(decoder_inputs, initial_state=final_state)
decoder_dense = Dense(num_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)
# Define the model that will turn
# `encoder_input_data` & `decoder_input_data` into `decoder_target_data`
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
opt = keras.optimizers.Adam(learning_rate=learning_rate)
# Run training
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

if mode == "train":

    model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
          batch_size=batch_size,
          epochs=epochs,
          validation_split=0.2)

    model.save_weights(modelsavename)
    exit()


if mode == "test":
    model.load_weights(modelsavename)


#infernece model
encoder_model = Model(encoder_inputs, final_state)
decoder_state_input_h = Input(shape=(latent_dim*2,))
decoder_states_inputs = [decoder_state_input_h]
decoder_outputs, state_h = decoder_gru(decoder_inputs, initial_state=decoder_state_input_h)
decoder_states = [state_h]
decoder_outputs = decoder_dense(decoder_outputs)
decoder_model = Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states)




reverse_input_char_index = dict((i, char) for char, i in token_index.items())
reverse_target_char_index = dict((i, char) for char, i in token_index.items())


#inference 
def decode_sequence(input_seq):
    
    # Encode the input as state vectors.
    encoder_out, states_value = encoder_model.predict(input_seq)
    encoder_out = [encoder_out]
    states_value = [states_value]
    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 1, num_tokens))
    # Populate the first character of target sequence with the start character.
    target_seq[0, 0, token_index['&']] = 1.

    # Sampling loop for a batch of sequences
    # (to simplify, here we assume a batch of size 1).
    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
        output_tokens, h = decoder_model.predict([target_seq] + states_value + encoder_out)

        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = reverse_target_char_index[sampled_token_index]
        decoded_sentence += sampled_char

        # Exit condition: either hit max length
        # or find stop character.
        if (sampled_char == '$' or
           len(decoded_sentence) > max_decoder_seq_length):
            stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1, 1, num_tokens))
        target_seq[0, 0, sampled_token_index] = 1.

        # Update states
        states_value = [h]

    return decoded_sentence












ans = []

#seq_index = list(range(len(encoder_input_data)))
#global passed
passed = 0
swa = ['़', 'ऽ', 'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'े', 'ै', 'ॉ', 'ो', 'ौ', '्','ँ', 'ं', 'ः', ':']
pre = ["अप", "ऩा", "दुर", "निर", "उप", "प्रति", "अप", "अभि", "अक", "परा", "महा", "परि", "त्रि", "अति", "मुख्य", "उच्च", "पूर्व", "प्रधान", "प्रमुख"]
#model output error correction code
def decode(ind):
    #if ind%100==0:
        #print("Mutiprocessing time: {}secs\n".format((time.perf_counter()-start)))
    input_seq = encoder_input_data[ind: ind + 1]
    
    decoded_sentence = decode_sequence(input_seq)
    decoded_sentence = decoded_sentence.strip()
    decoded_sentence = decoded_sentence.strip('$')
    #print(input_texts[ind],"---->", decoded_sentence,"   ",target_texts[ind],"\n")
    #decoded_sentence = decoded_sentence.split('+')
    splist = decoded_sentence.split('+')

    sp = len(splist[0])
    if len(splist)!=2 or len(input_texts[ind])-sp<4 or sp<4:
        return
    # sp += 1
    if splist[0] in pre:
        return
    
    endwi = input_texts[ind][sp+2:]
    if input_texts[ind][sp] in swa:
        if len(input_texts[ind])-(sp+1)<3:
            return
        # sp+=1
        # endwi = input_texts[ind][sp:]
        
    if splist[1].endswith(endwi) == False or splist[0].startswith(input_texts[ind][:sp-2]) == False:
        if splist[0][sp-1] == '्':
            sp = sp - 2
            if sp<4:
                return
        if input_texts[ind][sp] not in swa:
            ans.append(str(input_texts[ind] + '\t'+input_texts[ind][:sp]+'+'+input_texts[ind][sp:]+ '\t' + decoded_sentence))
        else:
            ans.append(str(input_texts[ind] + '\t'+input_texts[ind][:sp]+'+'+input_texts[ind][sp+1:]+ '\t' + decoded_sentence))
    else:
        if splist[1][0] not in swa:
            ans.append(str(input_texts[ind] + '\t'+decoded_sentence))
        else:
            ans.append(str(input_texts[ind] + '\t'+splist[0]+'+'+splist[1][1:]+ '\t' + decoded_sentence))

    # if decoded_sentence == target_texts[ind]:
    #     global passed
    #     passed = passed + 1
    return 



import sys
from tqdm import tqdm
if mode == "test":
    with open(lexicon_file) as fp:
        input_texts = fp.read().splitlines()



    encoder_input_data = np.zeros((len(input_texts), max_encoder_seq_length, num_tokens), dtype='float32')



    for i, input_text in enumerate(input_texts):
        for t, char in enumerate(input_text):
            try:
                encoder_input_data[i, t, token_index[char]] = 1.
            except:
                continue
        encoder_input_data[i, t + 1:, token_index['*']] = 1.



    #l = length of testing/lexicon data
    #ncore = no of multiprocessing cores
    #c = current no of core
    l = len(encoder_input_data)
    ncore = int(sys.argv[1])
    k = l//ncore
    c = int(sys.argv[2])*k



    start = time.perf_counter()
    for i in tqdm(range(c,min(c+k,l))):
        thread = []
        lll = min(k,l-c)
        for j in range(1):
            decode(i+j*lll)

    print("Mutiprocessing time: {}secs\n".format((time.perf_counter()-start)))




    file2 = open(lookupfile, 'a')
    for k in ans:
        file2.write(k+"\n")
    file2.close()
