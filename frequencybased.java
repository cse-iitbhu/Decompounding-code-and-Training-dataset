import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.*;
import java.nio.charset.Charset;
import java.util.*;

public class Emperical2 {
    static ArrayList<String> candidate = new ArrayList<>(); 
    static int len=0;

    
    static int frequencyCalc(String str) throws IOException {
        int c = 0;
        String line = "";

        char rem = (char) 65279;
        if (str.charAt(0) == rem)
            str = str.substring(1);

        try (
                
                InputStream fis = new FileInputStream("res2.txt");
                InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
                BufferedReader br = new BufferedReader(isr);
        ) {
            while ((line = br.readLine()) != null) {
                if (str.trim().equals(line.trim()))
                    c++;
            }
        }

        return c;
    }
    
    static int min(int x, int y, int z) {
        if (x <= y && x <= z) return x;

        if (y <= x && y <= z) return y;

        else return z;
    }

    
    static int editDist(String str1, String str2, int m, int n) {
        int dp[][] = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0)
                    dp[i][j] = j;

                else if (j == 0)
                    dp[i][j] = i;

                else if (str1.charAt(i - 1) == str2.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1];

                else
                    dp[i][j] = 1 + min(dp[i][j - 1],
                            dp[i - 1][j],
                            dp[i - 1][j - 1]);

            }
        }
        return dp[m][n];
    }

    
    static boolean isValid(String str) throws IOException {
        int c = 0;
       String line;

        str=str.trim();
        File file = new File("New Dictionary.txt");
        BufferedReader br2 = new BufferedReader(new FileReader(file));
        line = br2.readLine();

        while (line != null) {
            line=line.trim();

            if (str.equals(line))
                return true;

            line = br2.readLine();
        }
        br2.close();
        return false;
    }

    static double geometricMean(ArrayList<Integer> arr, int n) {
        double product = 1;

        for (int i = 0; i < n; i++)
            product = product * arr.get(i);

        double gm = (double) Math.pow(product, (double) 1 / n);
        return gm;
    }

    static void candidateGeneration1(String str, int comp, String original) throws IOException {
	FileWriter writer = new FileWriter("out.txt" , true);
        BufferedWriter bw = new BufferedWriter(writer);
        int min = str.length(), temp;
        boolean flag=false;
        String lastword = "";

        File file = new File("New Dictionary.txt");
        BufferedReader br2 = new BufferedReader(new FileReader(file));
        String line = br2.readLine();

        while(line != null){
	    line = line.trim();

            if(str.startsWith(line)) {
                temp = editDist(str, line, str.length(), line.length());

                if (min >= temp) {
                    flag=true;
                    min = temp;
                    lastword = line;
                }
            }
            //
            line = br2.readLine();
        }

        if(flag) {
            len = len + lastword.length();
            candidate.add(lastword);

            if (len < original.length()) {
                str = str.substring(lastword.length());
                candidateGeneration1(str, comp, original);
            }
            else {
		/*for(int r=0; r<candidate.size();r++)
			System.out.println(candidate.get(r));*/
                if(candidate.size()>1) {
                    ArrayList<Integer> geo = new ArrayList<>();

                    for (int i = 0; i < candidate.size(); i++)
                        geo.add(frequencyCalc(candidate.get(i)));

                    double sum = geometricMean(geo, geo.size());
                    if (comp > sum){
                        bw.write(original + "\t\t" + original);
			bw.newLine();
			}
                    else {
                        bw.write(original+ "\t\t");

                        for (int i = 0; i < candidate.size(); i++)
                            bw.write(candidate.get(i) + " ");

                        bw.newLine();
                    }
                }
                else{
                        bw.write(original + "\t\t" + original);
			bw.newLine();

		}
            }
        }
        else{
                bw.write(original + "\t\t" + original);
		bw.newLine();
		}
        bw.flush();
        br2.close();
        bw.close();
    }

    static void candidateGeneration(String str, int comp, String original) throws IOException {
        char rem=(char)65279;

        if(str.charAt(0)==rem)
            str=str.substring(1);

        if(original.charAt(0)==rem)
            original=original.substring(1);

        candidateGeneration1(str, comp, original);
    }
    public static void main(String args[]) throws IOException {
        String line;

        //Input file.
        File file = new File("new document.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        line = br.readLine();

        while (line != null){
            len=0;
            int x = frequencyCalc(line);
            candidateGeneration(line, x, line);
            candidate.clear();
            line = br.readLine();
        }
        br.close();
    }
}
