
//  Take name as input and print a greeting message for that name.

package com.company;

import java.util.Scanner;

public class Question_3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your name: ");

        String name = input.next();

        System.out.println("Welcome to the Java world, " + name + "!");

    }
}
