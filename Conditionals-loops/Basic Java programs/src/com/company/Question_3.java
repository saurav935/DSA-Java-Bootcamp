
// Area Of Rectangle Program

package com.company;

import java.util.Scanner;

public class Question_3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // // Taking length as input
        System.out.println("Enter the length of the rectangle: ");
        double length = input.nextDouble();

        // Taking breadth as input
        System.out.println("Enter the breadth of the rectangle: ");
        double breadth = input.nextDouble();

        System.out.println(length * breadth);
    }
}
