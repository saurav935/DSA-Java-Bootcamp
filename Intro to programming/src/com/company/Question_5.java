
// Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)

package com.company;

import java.util.Scanner;

public class Question_5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Taking first number as input
        System.out.print("Enter first number: ");
        double num_1 = input.nextDouble();

        // Taking second number as input
        System.out.print("Enter second number: ");
        double num_2 = input.nextDouble();

        // Taking character as input for operation
        System.out.print("Enter an operator: ");
        //String operator = input.next();
        String operator = input.next();


        if (operator == "*"){
            System.out.println(num_1 * num_2);
        }
        if (operator == "/"){
            System.out.println(num_1 / num_2);
        }
        if (operator == "+"){
            System.out.println(num_1 + num_2);
        }
        if (operator == "-"){
            System.out.println(num_1 - num_2);
        }




    }
}
