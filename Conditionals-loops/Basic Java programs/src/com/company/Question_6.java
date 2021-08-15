
// Area Of Rhombus

package com.company;

import java.util.Scanner;

public class Question_6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the length of first diagonal: ");
        double length_1 = input.nextDouble();

        System.out.println("Enter the length of the second diagonal: ");
        double length_2 = input.nextDouble();

        double area = (length_1 * length_2) / 2;

        System.out.println(area);

    }
}
