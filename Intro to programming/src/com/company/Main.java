package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number: ");     // here I have erased "ln" part from the Systems.out.print, because I want to use the same line
        int number = input.nextInt();
        int factorial = number;

        if(number == 0) {
            System.out.println(1);
        }

        while (number != 1)
        {
            factorial = factorial * (number - 1);
            number--;
        }
        System.out.println(factorial);

    }
}
