
//  Write a program to print whether a number is even or odd, also take input.

package com.company;

import org.w3c.dom.ls.LSOutput;

import java.util.Scanner;

public class Question_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = input.nextInt();

        if (number % 2 == 0){
            System.out.println("The number is even");

        }else{
            System.out.println("The number is odd");
        }
    }


}
