
// Area Of Isosceles Triangle

package com.company;

import java.util.Scanner;

public class Question_4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the length of isosceles triangle: ");
        double length = input.nextDouble();

        double area = (length * length) / 2;

        System.out.println(area);

    }
}
