package com.company;

import java.util.Scanner;

public class Question_10 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double max_ = Double.NEGATIVE_INFINITY;

        while (true){
            System.out.println("Enter a number: ");
            double number = input.nextDouble();
            max_ = Math.max(max_, number);
            if (number == 0){
                break;
            }
        }
        System.out.println(max_);
    }
}
