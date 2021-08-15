
// Area Of Triangle

package com.company;

import java.util.Scanner;

public class Question_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Input for base
        System.out.println("Enter base of the traingle: ");
        double base = input.nextDouble();

        // Input for height
        System.out.println("Enter height of the traingle: ");
        double height = input.nextDouble();

        double area = 0.5*base*height;

        System.out.println(area);
    }
}
