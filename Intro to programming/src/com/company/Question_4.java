
// Write a program to input principle, time and rate (P, T, R) from user and find Simple Interest.

package com.company;

import java.util.Scanner;

public class Question_4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Taking principal amount
        System.out.print("Enter principal amount: ");
        double P = input.nextDouble();

        // Taking time (in years)
        System.out.print("Enter time (in years): ");
        float T = input.nextFloat();

        // Taking rate of interest
        System.out.print("Enter annual rate of interest: ");
        double R = input.nextDouble();

        double amount = P * (1+R*T);

        System.out.println(amount);


    }
}
