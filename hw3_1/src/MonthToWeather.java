//***************************

// 파일명: monthWeather.java

// 작성자: 송혜주(202310940)

// 작성일: 2024-09-30

// 내용: 숫자를 입력받아 3~5는 "봄", 6~8는 "여름", 9~11는 "가을", 12, 1, 2는 "겨울"을 출력하는 프로그램을 작성

//***************************

import java.util.Scanner;

public class MonthToWeather {
    public static void main(String[] args) {
        System.out.println("hw3_1: 송혜주");
        System.out.println();

        Scanner scanner = new Scanner(System.in);
        int month = 0;
        do {
            System.out.print("월을 입력하세요: ");
            month = scanner.nextInt();
        } while (month < 1 || month > 12);

        switch(month) {
            case 3:
            case 4:
            case 5:
                System.out.println("봄");
                break;
            case 6:
            case 7:
            case 8:
                System.out.println("여름");
                break;
            case 9:
            case 10:
            case 11:
                System.out.println("가을");
                break;
            case 12:
            case 1:
            case 2:
                System.out.println("겨울");
                break;

        }
    }
}
