package app;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
	public static int gcm(int a, int b) {
	    return b == 0 ? a : gcm(b, a % b); 
	}
	public static String getMixed(int num, int den) {
		int wholeNum=0;
		String output="";
		while(num>=den) {
			num-=den;
			wholeNum+=1;
		}
		
		int newDen = gcm(num, den);
		num=num/newDen;
		den=den/newDen;
		if(num!=0&&wholeNum!=0) {
			output = Integer.toString(wholeNum) + " " + Integer.toString(num)+"/"+Integer.toString(den);
		}
		else if(wholeNum!=0&&num==0) {
			output = Integer.toString(wholeNum);
		}
		else if(wholeNum==0&&num!=0) {
			output = Integer.toString(num)+"/"+Integer.toString(den);
		}
		else if(wholeNum==0&&num==0){
			output = "0";
		}
		return output;
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(input.readLine());
		int den = Integer.parseInt(input.readLine());
		
		String output = getMixed(num, den);
		System.out.println(output);
	}

}
