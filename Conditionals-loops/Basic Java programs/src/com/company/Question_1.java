
// Area Of Circle Java Program

package com.company;

import java.util.Scanner;

public class Question_1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the radius of circle: ");

        double radius = input.nextDouble();

        double area = Math.PI*(radius*radius);

        System.out.println(area);
    }
}
