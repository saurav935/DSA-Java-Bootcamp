
// Calculate Average Of N Numbers

package com.company;

import java.util.Scanner;

public class Question_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter N: ");

        double n = input.nextDouble();
        double sum_ = input.nextDouble();

        for (double num = 1; num <= n; num+=1){
            sum_ += num;

        }
        System.out.println(sum_ / n);
    }
}
