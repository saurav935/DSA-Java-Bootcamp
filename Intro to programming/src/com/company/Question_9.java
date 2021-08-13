
// Take integer inputs till the user enters 0 and print the sum of all numbers (HINT: while loop)

package com.company;

import java.util.Scanner;

public class Question_9 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double summ = 0;

        while (true){
            System.out.println("Enter a number: ");
            double n = input.nextDouble();

            if (n != 0){
                summ += n;
            }else {
                break;
            }

        }
        System.out.println(summ);

    }
}
