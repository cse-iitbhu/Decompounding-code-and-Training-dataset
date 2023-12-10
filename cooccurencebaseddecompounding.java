import java.io.*;
import java.nio.charset.Charset;
import java.util.*;

public class BengaliSplitter {

    
    static boolean inDict(String str) throws IOException {
        char rem = (char) 65279;
        if (str.equals(""))
            return false;
        else {
            if (str.charAt(0) == rem)
                str = str.substring(1);

            String line;
            try (
                    
                    InputStream fis = new FileInputStream("New Dictionary.txt");
                    InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
                    BufferedReader br = new BufferedReader(isr);
            ) {
                while ((line = br.readLine()) != null) {
                    if (str.trim().equals(line.trim()))
                        return true;
                }
                return false;
            }
        }
    }

   
   static String applySandhi(String r)throws IOException {
       String s1, s2;
       char c1, c2;

       if(!r.equals("")) {
           if (r.charAt(0) == 'े') {
               c1 = 'इ';
               c2 = 'ई';
               s1 = r.replace(r.charAt(0), c1);
               s2 = r.replace(r.charAt(0), c2);

               if (inDict(s1))
                   return s1;

               else if(inDict(s2))
                   return s2;
           }

           if (r.charAt(0) == 'ो') {
               c1 = 'उ';
               c2 = 'ऊ';
               s1 = r.replace(r.charAt(0), c1);
               s2 = r.replace(r.charAt(0), c2);

               if (inDict(s1))
                   return s1;

               else if(inDict(s2))
                   return s2;
           }

           if (r.length() >=2 && r.substring(0, 2).equals("र्")) {
               s1 = r.replace(r.substring(0, 2), "");
               c1 = 'ऋ';
               c2 = 'ॠ';
               s2 = c1 + s1;
               String s3 = c2 + s1;

               if (inDict(s2))
                   return s2;

               else if(inDict(s3))
                   return (s3);
           }

           if (r.length() >=2 && r.substring(0, 2).equals("ल्")) {
               s1 = r.replace(r.substring(0, 2), "");
               s2 = "लृ" + s1;

               return s2;
           }
           //Vriddhi Sandhi
           if (r.charAt(0) == 'ै') {
               s1 = r.replace(r.charAt(0), 'ए');
               s2 = r.replace(r.charAt(0), 'ऐ');

               if (inDict(s1))
                   return s1;

               else if(inDict(s2))
                   return s2;
           }

           if (r.charAt(0) == 'ौ') {
               s1 = r.replace(r.charAt(0), 'औ');
               s2 = r.replace(r.charAt(0), 'ओ');

               if (inDict(s1))
                   return s1;

               else if(inDict(s2))
                   return s2;
           }

           if (r.charAt(0) == 'ा' && r.length() >=3 && r.substring(1, 3).equals("र्")) {
               c2 = r.charAt(0);
               s1 = r.replace(Character.toString(c2), "");
               s2 = s1.replace("र्", "");
               c1 = 'ऋ';
               s2 = c1 + s2;

               if(inDict(s2))
                   return s2;
           }

           if (r.charAt(0) == 'ा' && r.length() >=2 &&  r.substring(1, 3).equals("ल्")) {
               c2 = r.charAt(0);
               s1 = r.replace(Character.toString(c2), "");
               s2 = s1.replace("ल्", "");
               s2 = "लृ" + s2;

               if(inDict(s2))
                   return s2;
           }
           //Savrandirdh Sandhi
           else {
               if (r.charAt(0) == 'ा' || r.charAt(0) == 'ि' || r.charAt(0) == 'ी' || r.charAt(0) == 'ु' || r.charAt(0) == 'ू' || r.charAt(0) == 'ृ' || r.charAt(0) == 'े' || r.charAt(0) == 'ै' ||
                       r.charAt(0) == 'ो' || r.charAt(0) == 'ौ' || r.charAt(0) == 'ं' || r.charAt(0) == 'ः') {
                   s1 = Character.toString(r.charAt(0));
                   s1 = r.replace(s1, "");
                   s2 = 'अ' + s1;

                   if (inDict(s2))
                       return s2;

                   s2 = 'आ' + s1;
                   if (inDict(s2))
                       return s2;

                   s2 = 'इ' + s1;
                   if (inDict(s2))
                       return s2;

                   s2 = 'ई' + s1;
                   if (inDict(s2))
                       return s2;

                   s2 = 'उ' + s1;
                   if (inDict(s2))
                       return s2;

                   s2 = 'ऊ' + s1;
                   if (inDict(s2))
                       return s2;

                   s2 = 'ऋ' + s1;
                   if (inDict(s2))
                       return s2;

                   s2 = "लृ" + s1;
                   if (inDict(s2))
                       return s2;

                   else
                       return "null";
               }
               else
                   return "null";
           }
       }
       return "null";
   }

   
    static void candidateGeneration(String str) throws IOException {
        int count = 0;
        String s = "",r;
        int correct = 0;
        String pre = "",suf = "";

        FileWriter writer = new FileWriter("out.txt", true);
        BufferedWriter bw = new BufferedWriter(writer);

        HashMap<String, Integer> candidate = new HashMap<String, Integer>();

        for (int i = 1; i < str.length(); i++) {
            r="";
            String l = str.substring(0, i + 1);
            boolean z=false,y=false;

            if((i+1) < str.length())
                r = str.substring(i + 1);

            if (l.length() >=2 && !(l.equals(str)) /*&& r.length() >=3*/) {
                boolean x = inDict(l);
                y = inDict(r);

                if(x && !y) {
                    s = applySandhi(r);
                    z = !s.equals("null");

                    if (!z &&((str.charAt(i+1) >= 2305 && str.charAt(i+1) <= 2307) || (str.charAt(i+1) >= 2364 && str.charAt(i+1) <= 2384))){
                        l = l + str.charAt(i+1);
                        i++;

                        if((i+1) < str.length()) {
                            r = str.substring(i + 1);
                            y = inDict(r);
                        }
                    }
                }

                if (x && y) {
                    count++;
                    candidate.put(l, count);
                    candidate.put(r, count);
                    correct++;
                    pre = l;
                    suf = r;
                }

                else if (x && z /*&& s.length() >= 3*/) {
                    count++;
                    candidate.put(l, count);
                    candidate.put(s, count);
                    correct++;
                    pre = l;
                    suf = s;
                }

                else if (x) {
                    count++;
                    candidate.put(l, count);
                    if (!r.equals(""))
                        candidate.put(r, count);
                }

                else if (y) {
                    count++;
                    candidate.put(l, count);
                    candidate.put(r, count);
                }
            }
        }

        if(correct == 1) {
            bw.write(str + "\t\t" + pre + " " + suf);
            bw.newLine();
        }
        else
            bestSplit(candidate, count, str);

        bw.flush();
        bw.close();
    }

    
    static void bestSplit(HashMap<String, Integer> candidate, int count, String first)throws IOException {

        String compound[] = new String[50000];
        String constituents[] = new String[50000];
        String end[] = new String[8];
        int endcount = 0;
        int com = 0, cons = 0, common = 0;
        int endval[] = new int[4];
        double threshold = 0.02, overlap, max = 0.0;
        String l= "",r = "";

        File folder = new File("/home/siba/Desktop/puneet/Bengali/SanskritDocuments");
        File[] listOfFiles = folder.listFiles();

        FileWriter writer = new FileWriter("out.txt", true);
        BufferedWriter bw = new BufferedWriter(writer);

        if (candidate.size() >= 1) {
            for (int j = 0; j < listOfFiles.length; j++) {
                String path = "/home/siba/Desktop/puneet/Bengali/SanskritDocuments/";
                path = path + listOfFiles[j].getName();
                Scanner sc = new Scanner(new File(path));

                while (sc.hasNext()) {
                    String line = sc.next();
                    if (line.trim().equals(first.trim())) {
                        compound[com] = listOfFiles[j].getName();
                        com++;
                        break;
                    }
                }
                sc.close();
            }

            for (int i = 0; i < 5; i++) {
                ArrayList<String> can = new ArrayList<>();

                for (Map.Entry mapElement : candidate.entrySet()) {
                    String key = (String) mapElement.getKey();
                    int value = (int) mapElement.getValue();

                    if (i == value)
                        can.add(key);
                }

                for (int k = 0; k < can.size(); k++) {
                    String name = can.get(k);

                    for (int j = 0; j < listOfFiles.length; j++) {
                        String path = "/home/siba/Desktop/puneet/Bengali/SanskritDocuments/";
                        path = path + listOfFiles[j].getName();
                        Scanner sc = new Scanner(new File(path));

                        while (sc.hasNext()) {
                            String line = sc.next();
                            if (line.trim().equals(name.trim())) {
                                constituents[cons] = listOfFiles[j].getName();
                                cons++;
                                break;
                            }
                        }
                        sc.close();
                    }
                }

                for (int k = 0; k < com; k++) {
                    for (int j = 0; j < cons; j++) {

                        if (compound[k].equals(constituents[j]))
                            common++;
                    }
                }

                if (com != 0 && cons != 0) {
                    //Applying co occurrence measure.
                    overlap = ((float) common / (float) Math.min(com, cons));

                    if (overlap >= threshold) {
                        if (overlap > max) {
                            max = overlap;
                            l = can.get(0);
                            r = can.get(1);
                        }
                    }
                }

                constituents = new String[constituents.length];
                cons = 0;
                common = 0;
            }
        }

        if (max!=0.0)
            bw.write((first+ "\t\t" + l + " " + r));
        else
            bw.write(first + "\t\t" + first);

        bw.newLine();
        bw.flush();
        bw.close();
    }

    public static void main(String args[]) throws IOException {
        String line;
		char rem = (char) 65279;
        String affixes[] = { "प्र", "अधि", "परा" , "अति", "अप", "सु", "सम्", "उत्",
                "अनु", "अभि", "अव", "प्रति", "निर्", "परि", "दुर्", "उप", "वि", "नि" };

        try (
                //Input file
                InputStream fis = new FileInputStream("new document.txt");
                InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
                BufferedReader br = new BufferedReader(isr);

                //Output file
                FileWriter writer = new FileWriter("out.txt");
                BufferedWriter bw = new BufferedWriter(writer);
        ) {
            while ((line = br.readLine()) != null) {
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
                    candidateGeneration(line);

                bw.flush();
            }
        }
    }
}
