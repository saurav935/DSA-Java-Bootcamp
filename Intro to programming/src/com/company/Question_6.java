
// Take 2 numbers as input and print the largest number.

package com.company;

import java.util.Scanner;

public class Question_6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // First number input
        System.out.print("Enter first number: ");
        long num_1 = input.nextLong();

        // Second number input
        System.out.print("Enter second number: ");
        long num_2 = input.nextLong();

        if (num_1 > num_2){
            System.out.println(num_1 + " is greater");
        }else{
            System.out.println(num_2 + " is greater");
        }




    }
}
