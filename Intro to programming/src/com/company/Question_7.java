
// Input a number and print all the factors of that number (use loops).

package com.company;

import java.util.Scanner;

public class Question_7 {
    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        Scanner input = new Scanner(System.in);

        double number = input.nextDouble();

        for (int num = 1; num <= number; num += 1){
            if (number % num == 0){
                System.out.println(num);
            }
        }
    }
}
