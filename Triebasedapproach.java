import java.io.*;
import java.nio.charset.Charset;
import java.util.*;

class TrieNode
{
    char c;
    TrieNode parent;
    HashMap<Character, TrieNode> children = new HashMap<Character, TrieNode>();
    boolean isLeaf;

    public TrieNode() {}
    public TrieNode(char c){this.c = c;}
}

public class Trie {
    TrieNode root;
    ArrayList<String> prewords, sufwords, prefix, suffix;
    TrieNode prefixRoot;
    String curPrefix;
    boolean preenter, sufenter;

    public Trie() {
        root = new TrieNode();
        prewords = new ArrayList<String>(); 
        sufwords = new ArrayList<String>(); 
        prefix = new ArrayList<String>(); 
        suffix = new ArrayList<String>(); 
    }

    void inDictp(String word, String l, String str) throws IOException {
        String line, r="";
        boolean flag=false;
        File file = new File("trieout.txt");
        FileWriter fr = new FileWriter(file, true);
        BufferedWriter bw = new BufferedWriter(fr);

        try (
                
                InputStream fis = new FileInputStream("Sanskrit.txt");
                InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
                BufferedReader br = new BufferedReader(isr);
        ) {
            while ((line = br.readLine()) != null && !flag) {
                if (line.endsWith(str)){
                    r=line;
                    flag = applySandhi(word, l, line);
                }
            }
        }

        if(flag) {
            bw.write(word + " : " + l + " " + r);
            bw.newLine();
        }

        bw.flush();
        bw.close();
    }

    void inDicts(String word, String r, String str) throws IOException {
        String line, l="";
        boolean flag=false;
        File file = new File("trieout.txt");
        FileWriter fr = new FileWriter(file, true);
        BufferedWriter bw = new BufferedWriter(fr);

        try (
                
                InputStream fis = new FileInputStream("Sanskrit.txt");
                InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
                BufferedReader br = new BufferedReader(isr);
        ) {
            while ((line = br.readLine()) != null && !flag) {
                if (line.startsWith(str)){
                    l=line;
                    flag = applySandhi(word, line, r);
                }
            }
        }

        if(flag) {
            bw.write(word + " : " + l + " " + r);
            bw.newLine();
        }

        bw.flush();
        bw.close();
    }

    //Method to apply rules of Sandhi
    boolean applySandhi(String word, String l, String r) {
        //Guna Sandhi
        if(r.charAt(0) == 'इ' || r.charAt(0) == 'ई'){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) == 'ा'){
                c = l.charAt(l.length()-1);
                str = l.replace(Character.toString(c), "");
            }

            str=str+'े';
            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        if(r.charAt(0) == 'उ' || r.charAt(0) == 'ऊ'){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) == 'ा'){
                c = l.charAt(l.length()-1);
                str = l.replace(Character.toString(c), "");
            }

            str=str+'ो';
            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        if(r.charAt(0) == 'ऋ' || r.charAt(0) == 'ॠ'){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) == 'ा'){
                c = l.charAt(l.length()-1);
                str = l.replace(Character.toString(c), "");
            }

            str=str+"र्";
            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        //Vridhi Sandhi
        if(r.charAt(0) == 'ए' || r.charAt(0) == 'ऐ'){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) == 'ा'){
                c = l.charAt(l.length()-1);
                str = l.replace(Character.toString(c), "");
            }

            str=str+"ै";
            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        if(r.charAt(0) == 'ओ' || r.charAt(0) == 'औ'){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) == 'ा'){
                c = l.charAt(l.length()-1);
                str = l.replace(Character.toString(c), "");
            }

            str=str+"ौ";
            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        if(r.charAt(0) == 'ऋ'){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) != 'ा')
                str=str+'ा';

            str=str+"र्";
            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        if(r.substring(0, 2).equals("लृ")){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) != 'ा')
                str=str+'ा';

            str=str+"ल्";
            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        //Savrnadirdha sandhi
        if(r.charAt(0) == 'अ' || r.charAt(0) == 'आ'){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) != 'ा')
                str=str+'ा';

            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        if(r.charAt(0) == 'इ' || r.charAt(0) == 'ई'){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) != 'ी'){
                c=l.charAt(l.length()-1);
                str=l.replace(Character.toString(c),"");
            }

            str=str+'ी';
            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        if(r.charAt(0) == 'उ' || r.charAt(0) == 'ऊ'){
            String str=l;
            char c;

            if(l.charAt(l.length()-1) != 'ू'){
                c=l.charAt(l.length()-1);
                str=l.replace(Character.toString(c),"");
            }

            str=str+'ू';
            c=r.charAt(0);
            r=r.replace(Character.toString(c),"");
            str=str+r;

            return word.equals(str);
        }

        return false;
    }

    void insert(String word) {
        HashMap<Character, TrieNode> children = root.children;
        TrieNode crntparent;
        crntparent = root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            TrieNode t;

            if (children.containsKey(c)) {
                t = children.get(c);
            }
            else {
                t = new TrieNode(c);
                t.parent = crntparent;
                children.put(c, t);
            }

            children = t.children;
            crntparent = t;

            if (i == word.length() - 1)
                t.isLeaf = true;
        }
    }

    boolean search(String word) {
        TrieNode t = searchNode(word);

        if (t != null && t.isLeaf)
            return true;
        else
            return false;
    }

   
    boolean startsWith(String prefix) {
        if (searchNode(prefix) == null)
            return false;
        else
            return true;
    }

    TrieNode searchNode(String str) {
        Map<Character, TrieNode> children = root.children;
        TrieNode t = null;

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);

            if (children.containsKey(c)) {
                t = children.get(c);
                children = t.children;
            }
            else
                return null;
        }

        prefixRoot = t;
        curPrefix = str;
        return t;
    }

    
    void FindPrefix(TrieNode node) {
        if (node.isLeaf) {
            TrieNode altair = node;
            Stack<String> hstack = new Stack<String>();

            while (altair != prefixRoot) {
                hstack.push(Character.toString(altair.c));
                altair = altair.parent;
            }

            String wrd = curPrefix;
            while (!hstack.empty()) {
                wrd = wrd + hstack.pop();
            }

            preenter=true;
            if(!prewords.contains(wrd)){
                prewords.add(wrd);
            }
        }
        Set<Character> kset = node.children.keySet();
        Iterator itr = kset.iterator();
        ArrayList<Character> aloc = new ArrayList<Character>();

        while (itr.hasNext()) {
            Character ch = (Character) itr.next();
            aloc.add(ch);
        }

        for (int i = 0; i < aloc.size(); i++)
            FindPrefix(node.children.get(aloc.get(i)));
    }

   
    void FindSuffix(TrieNode node, String str) {
        if (!node.children.isEmpty()) {
            Set<Character> kset = node.children.keySet();
            Iterator itr = kset.iterator();
            ArrayList<Character> aloc = new ArrayList<Character>();

            while (itr.hasNext()) {
                Character ch = (Character) itr.next();
                aloc.add(ch);
            }

            for (int i = 0; i < aloc.size(); i++)
                FindSuffix(node.children.get(aloc.get(i)), str);
      }
        else {
            TrieNode temp = node;
            Stack<String> hstack = new Stack<String>();
            int len = str.length();
            String strtemp = "";

            for (int i = 0; i < len && temp!=root; i++) {
                hstack.push(Character.toString(temp.c));
                temp = temp.parent;
            }

            while (!hstack.empty()) {
                strtemp = strtemp + hstack.pop();
            }

            if (strtemp.equals(str)) {
                while (temp != root) {
                    hstack.push(Character.toString(temp.c));
                    temp = temp.parent;
                }

                strtemp = "";
                while (!hstack.empty()) {
                    strtemp = strtemp + hstack.pop();
                }

                strtemp = strtemp + str;
                //System.out.println(strtemp);
                sufenter=true;

                if(!sufwords.contains(strtemp)) {
                    sufwords.add(strtemp);
                }

            }
        }
    }

    
    void remove(TrieNode node, TrieNode depth) {
        TrieNode t=node.parent;

        if(node!=depth){
            if(node.children.isEmpty() && !node.isLeaf)
                node=null;

            remove(t, depth);
        }
    }

    public static void main(String args[]) throws IOException {
        String line;
        char rem = (char) 65279;
        boolean flag=false;
        Trie prefixTree = new Trie();
        String affixes[] = { "प्र", "अधि", "परा" , "अति", "अप", "सु", "सम्", "उत्",
                "अनु", "अभि", "अव", "प्रति", "निर्", "परि", "दुर्", "उप", "वि", "नि" };

        //Input file
        File file = new File("triein.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        //Output file
        FileWriter writer = new FileWriter("trieout.txt");
        BufferedWriter bw = new BufferedWriter(writer);

        //Lexicon file
        File lexfile = new File("trielexicon.txt");
        BufferedReader bl = new BufferedReader(new FileReader(lexfile));

        
        line = br.readLine();
        while(line != null) {
            boolean check = false;

            if (line.charAt(0) == rem)
                line = line.substring(1);

            for(int i = 0; i < affixes.length; i++) {
                if (line.startsWith(affixes[i]))
                    check = true;
            }

            if(check) {
                bw.write(line + "\t\t" + line);
                bw.newLine();
            }
            else
                prefixTree.insert(line);

            line = br.readLine();
        }

        line = bl.readLine();
        while (line != null){

            flag=false;
            prefixTree.preenter=false;
            prefixTree.sufenter=false;

            if (line.charAt(0) == rem)
                line = line.substring(1);

            //checking the Prefix suspicion list
            for(int i=0;i<prefixTree.prewords.size();i++){
                String find=prefixTree.prewords.get(i);

                if(find.endsWith(line)){
                    flag=true;
                    bw.write(find + "\t\t" + find.substring(0,find.indexOf(line)) + " " + line);
                    bw.newLine();
                    prefixTree.insert(find.substring(0,find.indexOf(line)));
                    TrieNode t = prefixTree.searchNode(find);
                    t.isLeaf=false;
                    prefixTree.remove(t, prefixTree.searchNode(find.substring(0,find.indexOf(line))));
                    prefixTree.insert(line);
                    prefixTree.prewords.remove(i);
                }
            }

            
            if(!flag){
                for(int i=0;i<prefixTree.sufwords.size();i++){
                    String find=prefixTree.sufwords.get(i);

                    if(find.startsWith(line)){
                        flag=true;
                        bw.write(find + "\t\t"+ line + " " + find.substring(line.length()));
                        bw.newLine();
                        prefixTree.insert(line);
                        TrieNode t = prefixTree.searchNode(find);
                        t.isLeaf=false;
                        prefixTree.remove(t, prefixTree.searchNode(line));
                        prefixTree.insert(find.substring(line.length()));
                        prefixTree.sufwords.remove(i);
                    }
                }
            }

            
            if (prefixTree.startsWith(line)) {
                TrieNode tn = prefixTree.searchNode(line);
                prefixTree.FindPrefix(tn);
            }

            
            if(!prefixTree.preenter)
                prefixTree.FindSuffix(prefixTree.root, line);

            
            if(prefixTree.preenter){
                prefixTree.prefix.add(line);

                for(int i=0 ;i<prefixTree.prewords.size(); i++){
                    String str = prefixTree.prewords.get(i);

                    if(str.startsWith(line)){
                        if(prefixTree.search(str.substring(line.length()))){
                            bw.write( str + ": " + line + " " + str.substring(line.length()));
                            bw.newLine();
                            prefixTree.prewords.remove(i);
                        }
                    }
                }
            }

            
            if(prefixTree.sufenter){
                prefixTree.suffix.add(line);

                for(int i=0; i<prefixTree.sufwords.size(); i++){
                    String str = prefixTree.sufwords.get(i);

                    if(str.endsWith(line)){
                        if(prefixTree.search(str.substring(0,str.indexOf(line)))){
                            bw.write(str + ": " + str.substring(0,str.indexOf(line)) + " " + line);
                            bw.newLine();
                            prefixTree.sufwords.remove(i);
                        }
                    }
                }
            }

           

            bw.flush();
            line = bl.readLine();
        }

        
        if(!prefixTree.prewords.isEmpty()){
            for(int i=0; i<prefixTree.prefix.size(); i++){
                String str=prefixTree.prefix.get(i);

                for(int j=0; j<prefixTree.prewords.size(); j++){
                    String chk=prefixTree.prewords.get(j);
                    String find;

                    if(chk.startsWith(str)){
                        if(chk.charAt(chk.length()-1) == 'ः')
                            find = chk.substring(chk.length() - 2);
                        else
                            find = Character.toString(chk.charAt(chk.length()-1));

                        prefixTree.inDictp(chk, str, find);
                    }
                }
            }
        }

        
        if(!prefixTree.sufwords.isEmpty()){
            for(int i=0; i<prefixTree.suffix.size(); i++){
                String str=prefixTree.suffix.get(i);

                for(int j=0; j<prefixTree.sufwords.size(); j++){
                    String chk=prefixTree.sufwords.get(j);
                    String find;

                    if(chk.endsWith(str)){
                        find = chk.substring(0,2);

                        prefixTree.inDicts(chk, str, find);
                    }
                }
            }
        }
        bw.close();
    }
}
