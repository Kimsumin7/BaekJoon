package forWhile;

import java.util.Scanner;

public class Ex01 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		
		//유효성 검사
		if (N < 1 || N >9) {
			System.out.println("1~9사이의 수 입력>>");
			return;
		}
		
		for (int i = 1; i <= 9; i++) {
			System.out.println(N + "*" + i + "=" + (N*i));
			
		}

	}

}
