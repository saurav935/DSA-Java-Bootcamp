
// Factorial Program In Java

package com.company;

import java.util.Scanner;

public class Question_1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the number: ");

        double n = input.nextDouble();

        if (n == 0){
            System.out.println("The factorial is: " + 1);
        }
        double ans = 1;

        while (n > 1){
            ans *= n;
            n -= 1;



        }
        System.out.println("The factorial is: " + ans);
    }
}
