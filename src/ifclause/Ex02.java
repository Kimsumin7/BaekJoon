package ifclause;

import java.util.Scanner;

public class Ex02 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int grade = scanner.nextInt();
		
		if (90 < grade < 100) {
			System.out.println("A");
		}

	}

}
