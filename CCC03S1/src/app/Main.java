package app;


import java.util.Scanner;

public class Main {
	public static int[] boardGen() {
		int[] board = new int[100];
		for(int i=0;i<board.length;i++) {  //O(n) complexity
			board[i] = 0;
		}
		board[0]=1;
		return board;
	}
	public static void setNew(int[]board, int moves) {
		boolean found=false;
		for(int i=0;!found;i++) {  //O(n) complexity
			if(board[i]==1) {
				if(i==99) {
					System.out.println("You are now on square 100");
					System.out.println("You Win!");
					break;
				
					
				}
				else if(i+moves==89) {
					board[47]=1;
					System.out.println("You are now on square " + 48);
				}
				else if(i+moves==98) {
					board[76]=1;
					System.out.println("You are now on square " + 77);
				}
				else if(i+moves==53) {
					board[18]=1;
					System.out.println("You are now on square " + 19);
				}
				else if(i+moves==8) {
					board[33]=1;
					System.out.println("You are now on square " + 34);
				}
				else if(i+moves==39) {
					board[63]=1;
					System.out.println("You are now on square " + 64);
				}
				else if(i+moves==66) {
					board[85]=1;
					System.out.println("You are now on square " + 86);
				}
				else if(i+moves>99) {
					System.out.println("You are now on square " + (i+1));
					found = true;
					break;
	
				}
				else {
				board[i+moves]=1;
				System.out.println("You are now on square " + (i+1+moves));
				}
				
				board[i]=0;
				found=true;
				break;
				
			}
		}
		
	}
	
	public static void main(String args[]) {
		boolean win = false;
		Scanner input = new Scanner(System.in);
		
		int[] board = boardGen();
		while(!win) { //O(n^2)
			int moves = Integer.parseInt(input.nextLine());
			if(moves==0) {
				System.out.println("You Quit!");
				
				break;
			}
			setNew(board, moves);
			
			if(board[99]==1) {
				
				System.out.println("You Win!");
				break;
			}
		}
		
		
		
	}
}
