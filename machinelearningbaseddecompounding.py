
import pandas as pd
import glob
import numpy as np


hasw_swar=[b'\xe0\xa4\x85', b'\xe0\xa4\x87', b'\xe0\xa4\x89', b'\xe0\xa4\x8b']
dirgha_swar=[b'\xe0\xa4\x86', b'\xe0\xa4\x88',b'\xe0\xa4\x8a', b'\xe0\xa4\x8f', b'\xe0\xa4\x90',b'\xe0\xa4\x93',b'\xe0\xa4\x94']
vyanjan=[b'\xe0\xa4\x95', b'\xe0\xa4\x96', b'\xe0\xa4\x97', b'\xe0\xa4\x98', b'\xe0\xa4\x99',b'\xe0\xa4\x9a', b'\xe0\xa4\x9b', b'\xe0\xa4\x9c', b'\xe0\xa4\x9d',b'\xe0\xa4\x9e',
         b'\xe0\xa4\x9f',b'\xe0\xa4\xa0', b'\xe0\xa4\xa1', b'\xe0\xa4\xa2',b'\xe0\xa4\xa3',b'\xe0\xa4\xa4',b'\xe0\xa4\xa5',b'\xe0\xa4\xa6',b'\xe0\xa4\xa7',b'\xe0\xa4\xa8',
         b'\xe0\xa4\xaa',b'\xe0\xa4\xab',b'\xe0\xa4\xac', b'\xe0\xa4\xad',b'\xe0\xa4\xae' ,b'\xe0\xa4\xaf', b'\xe0\xa4\xb0', b'\xe0\xa4\xb2',b'\xe0\xa4\xb5',b'\xe0\xa4\xb6',
         b'\xe0\xa4\xb7',b'\xe0\xa4\xb8', b'\xe0\xa4\xb9']
visarg=[b'\xe0\xa4\x83']
matra=[b'\xe0\xa4\xbe',b'\xe0\xa4\xbf',b'\xe0\xa5\x80',b'\xe0\xa5\x81',b'\xe0\xa5\x82',b'\xe0\xa5\x83',b'\xe0\xa5\x87',b'\xe0\xa5\x88',b'\xe0\xa5\x8b',b'\xe0\xa5\x8c']
half=[b'\xe0\xa5\x8d']


def get_sandhi_dataset(datafile):
     
     with open(datafile, encoding='utf8') as fp:
        tests = fp.read().splitlines()
     
        datalist=[]
        for test in tests:
            s_segment2=b'\xe0\xa5\xaf'
            x=test.encode('UTF-8')
            if(test.find('=>') == -1):
                continue;
            inout = test.split('=>')
            words = inout[1].split('+')
            if(len(words) > 2):
                continue;
            segment1 = words[0].strip()
            s_segment1=segment1.encode('UTF-8')
            if(len(words)>1):
                segment2 = words[1].strip()
                s_segment2=segment2.encode('UTF-8')
            segment3 = inout[0].strip()
            segment3 = segment3.split(" ")[-1]
            s_segment3=segment3.encode('UTF-8')
            
            datalist.append([s_segment1,s_segment2,s_segment3])
        data_sandhi = pd.DataFrame(datalist, columns = ['word1','word2','fullword'])
        return data_sandhi
 
def get_xy_data(datafile):
    dl = get_sandhi_dataset(datafile)
    return dl
    


df=get_xy_data("outputttt.txt")
df.shape


letter_list = [ 
    b'\xe0\xa4\x85', b'\xe0\xa4\x87', b'\xe0\xa4\x89', b'\xe0\xa4\x8b',
    b'\xe0\xa4\x82',
    b'\xe0\xa4\x86', b'\xe0\xa4\x88',b'\xe0\xa4\x8a', b'\xe0\xa4\x8f', b'\xe0\xa4\x90',b'\xe0\xa4\x93',b'\xe0\xa4\x94',
    b'\xe0\xa4\x95', b'\xe0\xa4\x96', b'\xe0\xa4\x97', b'\xe0\xa4\x98', b'\xe0\xa4\x99',b'\xe0\xa4\x9a', b'\xe0\xa4\x9b', b'\xe0\xa4\x9c', b'\xe0\xa4\x9d',b'\xe0\xa4\x9e',
         b'\xe0\xa4\x9f',b'\xe0\xa4\xa0', b'\xe0\xa4\xa1', b'\xe0\xa4\xa2',b'\xe0\xa4\xa3',b'\xe0\xa4\xa4',b'\xe0\xa4\xa5',b'\xe0\xa4\xa6',b'\xe0\xa4\xa7',b'\xe0\xa4\xa8',
         b'\xe0\xa4\xaa',b'\xe0\xa4\xab',b'\xe0\xa4\xac', b'\xe0\xa4\xad',b'\xe0\xa4\xae' ,b'\xe0\xa4\xaf', b'\xe0\xa4\xb0', b'\xe0\xa4\xb2',b'\xe0\xa4\xb5',b'\xe0\xa4\xb6',
         b'\xe0\xa4\xb7',b'\xe0\xa4\xb8', b'\xe0\xa4\xb9',
    b'\xe0\xa4\x83',
    b'\xe0\xa4\xbe',b'\xe0\xa4\xbf',b'\xe0\xa5\x80',b'\xe0\xa5\x81',b'\xe0\xa5\x82',b'\xe0\xa5\x83',b'\xe0\xa5\x87',b'\xe0\xa5\x88',b'\xe0\xa5\x8b',b'\xe0\xa5\x8c',
    b'\xe0\xa5\x8d',b'\xe0\xa4\xbc',b'',b'\xe0\xa4\x81',b'\xe0\xa4\x99',b'\xe0\xa5\x9c',b'\xe0\xa5\xaf',b'\xe0\xa4\xbd',b':'
]
vyanjan_sandh=[b'\xe0\xa4\x97',b'\xe0\xa4\x9c',b'\xe0\xa4\xa1',b'\xe0\xa4\xa6',b'\xe0\xa4\xac']
dirgh_lst = [matra[0],matra[2],matra[4]]
gun_lst = [matra[6],matra[8],matra[5]]
vrydhi_lst = [matra[7],matra[9]]
symb=[  b'\xe0\xa4\x82',  b'\xe0\xa4\x83',
    b'\xe0\xa4\xbe',b'\xe0\xa4\xbf',b'\xe0\xa5\x80',b'\xe0\xa5\x81',b'\xe0\xa5\x82',b'\xe0\xa5\x83',b'\xe0\xa5\x87',b'\xe0\xa5\x88',
    b'\xe0\xa5\x8b',b'\xe0\xa5\x8c', b'\xe0\xa5\x8d',b'\xe0\xa4\xbc',b'',b'\xe0\xa4\x81',b'\xe0\xa4\x99']


letter_dict = {}
for i,letter in enumerate(letter_list):

    letter_dict[letter.decode()] = i
reversed_dictionary = {value : key for (key, value) in letter_dict.items()}

def get_sandhi_dataset(datafile):
     with open(datafile, encoding='utf8') as fp:
        tests = fp.read().splitlines()
        datalist=[]
        for test in tests:
            x=test.encode('UTF-8')
            datalist.append(test.strip())
        return datalist
 
def get_xy_pre(datafile):
    dl = get_sandhi_dataset(datafile)
    return dl


lst=[]
pre=[]
lst=get_xy_pre("lst.txt")
pre=get_xy_pre("pre.txt")
lst.sort(key=len,reverse=True)




training_input = [[]]
training_output = [[]]
count=0
ans=[]
lett={}
pre_lst=[]
bl=''
b=0
ss="ऽ"
for index in range(len(df['fullword'])):  
    fullword = df['fullword'][index].decode('utf-8-sig')
    #print(fullword)
    if(ss in fullword):
                        ff=fullword.find(ss)
                        print(fullword,ff)
                        continue
    u=((df['word1'][index].decode('utf-8-sig')+df['word2'][index].decode('utf-8-sig')).encode('UTF-8'))
    v=((df['fullword'][index]).decode('utf-8-sig').encode('UTF-8'))
    for i,letter in enumerate(fullword):
         q=0
         z=0
         if(u==v):
                     b+=1
                     if(df['fullword'][index].decode('utf-8-sig') not in lst):
                         lst.append(df['fullword'][index].decode('utf-8-sig'))
                     if(df['word1'][index].decode('utf-8-sig') not in lst):
                         lst.append(df['word1'][index].decode('utf-8-sig'))
                     if(df['word2'][index].decode('utf-8-sig') not in lst):
                         lst.append(df['word2'][index].decode('utf-8-sig'))
                     for k,le in enumerate(lst):
                        lett[le] = k+65
         if((df['word1'][index].decode('utf-8-sig')).encode('UTF-8')==v):
                  z=1
                  pre_lst.append(fullword)
                  break
         if(z==1):
            break
         if(u==v):
            for j in (ans):
                
                if(j in fullword):
                        q=1
                        training_input[0].append(letter_dict[bl])
                        training_input[1].append(lett[fullword])
                        training_input[2].append(letter_dict[bl])
                        training_output[0].append(lett[df['word1'][index].decode('utf-8-sig')])
                        training_output[1].append(letter_dict[bl]) 
                        training_output[2].append(lett[df['word2'][index].decode('utf-8-sig')])
                        break
                 
         if(q==1):
            break
         if ((i!=0) and (i!=1) and (i<len(fullword)-1))and(letter.encode() in dirgh_lst):
                if (letter.encode() == matra[0]):
                        training_input[0].append(letter_dict[df['fullword'][index].decode()[i]])
                        #print(fullword)
                 
                        if((df['word1'][index].decode()[-1]).encode() == matra[0]):
                            training_output[0].append(letter_dict[df['word1'][index].decode()[-1]])
                            break
                      
                        else:
                            training_output[0].append(letter_dict[''])
                            break
                            
                       
                elif (letter.encode() == matra[2]):
                        #print(fullword)
                        training_input[0].append(letter_dict[df['fullword'][index].decode()[i]])
             
                        if((df['word1'][index].decode()[-1]).encode() == matra[2]):
                            training_output[0].append(letter_dict[df['word1'][index].decode()[-1]])
                            break
                            
                        else:
                            training_output[0].append(letter_dict[''])
                            break
                         
             
                elif (letter.encode() == matra[4]):
                        #print(fullword)
                        training_input[0].append(letter_dict[df['fullword'][index].decode()[i]])
                    
                        if((df['word1'][index].decode()[-1]).encode() == matra[2]):
                            training_output[0].append(letter_dict[df['word1'][index].decode()[-1]])
                            break
                            
                        else:
                            training_output[0].append(letter_dict[''])
                            break
                           
         elif ((i!=0) and (i!=1) and (i<len(fullword)-1))and(letter.encode() in gun_lst):
                  if (letter.encode() == matra[6]):
                        training_input[0].append(letter_dict[df['fullword'][index].decode()[i]])
                
                       
                        if((df['word1'][index].decode()[-1]).encode() == matra[6]):
                            training_output[0].append(letter_dict[df['word1'][index].decode()[-1]])
                            break
                         
                        else:
                            training_output[0].append(letter_dict[''])
                            break
                          
                  elif (letter.encode() == matra[5]):
                        #print(fullword)
                        training_input[0].append(letter_dict[df['fullword'][index].decode()[i]])
                       
               
                        if((df['word1'][index].decode()[-1]).encode() == matra[5]):
                            training_output[0].append(letter_dict[df['word1'][index].decode()[-1]])
                            break
                        
                        else:
                            training_output[0].append(letter_dict[''])
                            break
                           
         else:
                    continue
training_input = np.array(training_input).T
training_output=np.array(training_output).T
print(training_input.shape)
print(training_input.size)
print(training_output.shape)
print(training_output.size) 




from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
X_train, X_test, y_train, y_test = train_test_split(training_input, training_output, test_size=0.2, random_state=2)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
clf = OneVsRestClassifier(SVC())
clf.fit(X_train, y_train)
c=0
y_pred=clf.predict(X_test)
for i in range(len(y_pred)):
 if(y_test[i]==y_pred[i]):
  c+=1
print("ACCURACY =",c/len(y_pred))




'''
with open('/content/drive/MyDrive/sansoutt.txt','w') as out:
   out.write(' abcd \n')
'''



def get_sandhi_d(qq):
  y=0
  for test in qq:
                    if(test.encode('UTF-8') in letter_list):
                        continue
                    else:
                        y=1
                        break
  if(y==1):
    return False
  else:
    return True
 


'''
dff=get_xy_d("/content/drive/MyDrive/input.txt")
dff.shape
'''



import os
import numpy as np
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')




import zipfile
with zipfile.ZipFile("alreadydoneuniq.zip","r") as zip_ref:
    zip_ref.extractall("checkk")


c=0

files = glob.glob('checkk/alreadydoneuniq/*.txt')
for fle in files:
    c=c+1
print(c)



'''
files = glob.glob("/content/ne/*.txt") 
c=0
for fle in files:
  c=c+1
  corpus=[]
  nel=[]
  with open(fle, encoding="utf8", errors='ignore') as f:
    lines=f.read()
    qw=lines.split("\n")
    for i in qw:
      if(i.strip()!=""):
        nel.append(i)
  print(nel)
  with open(fle,'w',encoding="utf8", errors='ignore') as f:
    for i in nel:
      f.write("%s\n"%(i))
  with open(fle, encoding="utf8", errors='ignore') as f:
        text = f.read()
        corpus.append(text)
  
  text.strip()
  new=[]
  for i in corpus:
       a=str(i)[26:-16]
       new.append(a.replace('\n', ' ').replace('\u200c', ' ').replace('>', '').replace('HEAD', '').replace('HL','').replace('TEXT','').replace('<', '').replace('/', '').replace('HEAD', '').replace('BODY', '').replace('\xa0', '').replace('DOC', '').replace('\u200d', ' ').replace('-', ' ').replace(',', ' ').replace(':', ' ').replace('.', ' ').replace('\'', ' ').replace('|', ' ').replace('(',' ').replace(')', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace('.', ' ').replace('।', ' ').replace('-', ' ').replace('|', ' '))
  m=text.split("\n")
  with open(fle,'w') as f:
        f.write("%s\n"%(m[0]))
  s="\n".join(m[:-3])
  for i in range(len(s)):
    #print(s[i]) 
    with open(fle,'a') as f:
        f.write(s[i])
  with open(fle,'a') as f:
        f.write("\n")
  #print(text)
  corpus=new
  r=0
  for i in range(len(corpus)):
    for word in nltk.word_tokenize((corpus[i])):
          r=r+1
          print(word)
          with open(fle,'a') as f:
           f.write("%s\n"%((word)))
  print("%s\n"%("</TEXT>"))
  print("%s\n"%("</DOC>"))
  with open(fle,'a') as f:
        f.write("%s\n"%(("</TEXT>")))
        f.write("%s\n"%(("</DOC>")))
  
for fle in files:
  c=c+1
  corpus=[]
  with open(fle, encoding="utf8", errors='ignore') as f:
        text = f.read()
print(text)
'''




ss="ऽ"
pre=get_xy_pre("pre.txt")
lst=get_xy_pre("lst.txt")
files = glob.glob("checkk/alreadydoneuniq/*.txt") 
c=1
for fle in files:
  c=c+1
  corpus=[]
  nel=[]
  with open(fle, encoding="utf8", errors='ignore') as f:
    lines=f.read()
    qw=lines.split("\n")
    for i in qw:
      if(i.strip()!=""):
        nel.append(i)
  with open(fle,'w',encoding="utf8", errors='ignore') as f:
    for i in nel:
      f.write("%s\n"%(i))
  with open(fle, encoding="utf8", errors='ignore') as f:
        text = f.read()
        corpus.append(text)
  new=[]
  text.strip()
  m=text.split("\n")
  for i in corpus:
       a=str(i)[26:-16]
       new.append(a.replace('\n', ' ').replace('\u200c', ' ').replace('>', '').replace('HEAD', '').replace('text','').replace('HL','').replace('TEXT','').replace('<', '').replace('/', '').replace('docno','').replace('HEAD', '').replace('BODY', '').replace('\xa0', '').replace('DOC', '').replace('doc','').replace('\u200d', ' ').replace('-', ' ').replace(',', ' ').replace(':', ' ').replace('.', ' ').replace('\'', ' ').replace('|', ' ').replace('(',' ').replace(')', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace('.', ' ').replace('।', ' ').replace('-', ' ').replace('|', ' '))
  with open(fle,'w') as f:
        f.write("%s\n"%(m[0]))
  #print(m[0])
  s="\n".join(m[:-3])
  for i in range(len(s)):
    #print(s[i]) 
    with open(fle,'a') as f:
        f.write(s[i])
  with open(fle,'a') as f:
        f.write("\n")
  #print(text)
  corpus=new
  r=0
  #print(corpus[0])
  for i in range(len(corpus)):
    for word in nltk.word_tokenize((corpus[i])):
        print(word)
        r=r+1
        if( word[0]=='D'):
         fullword=word[1:len(word)]
        elif( word[0]=='A'):
         fullword=word[2:len(word)]
        elif( word[0]=='E'):
         fullword=word[3:len(word)]
        elif( word[0]=='H'):
         fullword=word[4:len(word)]
        else:
          fullword=word
        fullword.strip()
        if(get_sandhi_d(fullword)==True):
          if(ss in fullword):
                        ff=fullword.find(ss)
                        #print(fullword,ff)
                        s=fullword[0:ff]
                        s1="अ"+fullword[ff+1:len(fullword)]
                        ll=20-len(s)
                        with open(fle,'a') as f:
                          f.write("%s%s%s\n"%((s),(ll*" "),(s1)))
                        #print(fullword,"\t",s," ",s1)
                        #lst.append(s)
                        #lst.append(s1)
                        continue
          for i,letter in enumerate(fullword):
            v=0
            z=0
            if((len(fullword)>3 and len(fullword)<=8) or (len(fullword)>20)):
              lst.append(fullword)
              lst.sort(key=len,reverse=True) 
              pp=25-len(fullword)
              with open(fle,'a') as out:
                out.write("%s\n"%((fullword)))
              #print(fullword)
              break
            for j in (pre):
                if(j in fullword):
                    z=1
                    #print(fullword,"\t","\t",fullword)
                    pp=25-len(fullword)
                    with open(fle,'a') as out:
                      out.write("%s\n"%((fullword)))
                    break
            if(z==1):
                break
            for j in (lst):
                if(j in fullword):
                    if(len(fullword)-len(j)>3 and fullword[len(j)].encode('UTF-8') not in symb):
                        v=1
                        s=""
                        s1=""
                        s=fullword[0:len(j)]
                        if(fullword[len(j)].encode("UTF-8") in half):
                            s1=fullword[len(j)-1]
                        s1+=fullword[len(j):len(fullword)]
                        pp=25-(len(fullword));
                        ll=20-len(s)
                        with open(fle,'a') as f:
                          f.write("%s%s%s\n"%((s),(ll*" "),(s1)))
                        break
                    else:
                        v=1
                        print(fullword,"\t","\t",fullword)
                        pp=len(fullword)
                        with open(fle,'a') as out:
                          out.write("%s\n"%((fullword)))
                        break
                        
                        
            if(v==1):
              break
            if ((i!=0) and (i!=1) and (i<len(fullword)-1))and(letter.encode() in dirgh_lst):
                if (letter.encode() == matra[0]):
                        
                            s=""
                            s1=""
                            s+=(fullword)[0:i]
                            s1+=(fullword)[i+1:len(fullword)] 
                            if(clf.predict(letter_dict[fullword[i]])<65):
                                s+=(reversed_dictionary[clf.predict(letter_dict[fullword[i]])])
                            pp=25-(len(fullword));
                            ll=20-len(s)
                            with open(fle,'a') as f:
                              f.write("%s%s%s\n"%((s),(ll*" "),(s1)))
                 
 
                            
                       
                elif (letter.encode() == matra[2]):
                        #print(fullword)
                        s=""
                        s1=""
                        s+=(fullword)[0:i]
                        s1+=(fullword)[i+1:len(fullword)] 
                        if(clf.predict(letter_dict[fullword[i]])<65):
                            s+=(reversed_dictionary[clf.predict(letter_dict[fullword[i]])])
                        pp=25-(len(fullword));
                        ll=20-len(s)
                        with open(fle,'a') as f:
                          f.write("%s%s%s\n"%((s),(ll*" "),(s1)))
                         
             
                elif (letter.encode() == matra[4]):
                        #print(fullword)
                        s=""
                        s1=""
                        s+=(fullword)[0:i]
                        s1+=(fullword)[i+1:len(fullword)] 
                        if(clf.predict(letter_dict[fullword[i]])<65):
                            s+=(reversed_dictionary[clf.predict(letter_dict[fullword[i]])])
                        pp=25-(len(fullword));
                        ll=20-len(s)
                        with open(fle,'a') as f:
                          f.write("%s%s%s\n"%((s),(ll*" "),(s1)))
                        
                           
            elif ((i!=0) and (i!=1) and (i<len(fullword)-1))and(letter.encode() in gun_lst):
                  if (letter.encode() == matra[6]):
                        s=""
                        s1=""
                        s+=(fullword)[0:i]
                        s1+=(fullword)[i+1:len(fullword)] 
                        if(clf.predict(letter_dict[fullword[i]])<65):
                            s+=(reversed_dictionary[clf.predict(letter_dict[fullword[i]])])
                        pp=25-(len(fullword));
                        ll=20-len(s)
                        with open(fle,'a') as f:
                          f.write("%s%s%s\n"%((s),(ll*" "),(s1)))
                          
                  elif (letter.encode() == matra[5]):
                        #print(fullword)
                        s=""
                        s1=""
                        s+=(fullword)[0:i]
                        s1+=(fullword)[i+1:len(fullword)] 
                        if(clf.predict(letter_dict[fullword[i]])<65):
                            s+=(reversed_dictionary[clf.predict(letter_dict[fullword[i]])])
                        pp=25-(len(fullword));
                        ll=20-len(s)
                        with open(fle,'a') as f:
                          f.write("%s%s%s\n"%((s),(ll*" "),(s1)))
                           
            else:
                    with open(fle,'a') as out:
                     out.write("%s\n"%((fullword)))
  with open(fle,'a') as f:
    f.write("%s\n"%(("</BODY>")))
    f.write("%s\n"%(("</DOC>"))) 
  nell=[]
  with open(fle, encoding="utf8", errors='ignore') as f:
    lines=f.read()
    qw=lines.split("\n")
    for i in qw:
        nell.append(i.strip())
  with open(fle,'w',encoding="utf8", errors='ignore') as f:
    for i in nell:
      f.write("%s\n"%(i))
print(pre)



