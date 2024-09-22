//***************************

// 파일명: BirthDate.java

// 작성자: 송혜주 (202310940)

// 작성일: 2024-09-22

// 내용: 주민등록번호로부터 생년월일을 알아보는 프로그램, 조건문은 사용하지 않고 연산자 이용

//***************************

import java.util.Scanner;

public class BirthDate {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("hw2_1: 송혜주");
        System.out.println();
        System.out.print("주민등록번호 앞자리 입력: ");
        int frontNumber = scanner.nextInt();
        System.out.print("주민등록번호 뒷자리 입력: ");
        int backNumber = scanner.nextInt();

        int era = (backNumber / 1000000 < 3) ? 19 : 20;
        int year = frontNumber / 10000;
        int month = (frontNumber - year * 10000) / 100;
        int day = (frontNumber - year * 10000) - month * 100;

        System.out.println("생년월일은 다음과 같습니다.");
        System.out.print(era);
        String zero = year < 10 ? "0" : "";
        System.out.println(zero + year);
        System.out.println(month);
        System.out.println(day);


    }
}