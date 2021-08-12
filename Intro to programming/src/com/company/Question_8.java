
//  Input currency in rupee and output in dollar.

package com.company;

import java.util.Scanner;

public class Question_8 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Taking amount in Rupee
        System.out.println("Enter the currency in rupee: ");
        double amount = input.nextDouble();

        // Performing conversion
        double converted_amount = amount * 0.013;   // the rate of conversion keeps on changing

        System.out.println("The amount in dollar is: " + converted_amount);
    }
}
