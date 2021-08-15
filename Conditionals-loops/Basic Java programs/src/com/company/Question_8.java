
// Perimeter Of Circle

package com.company;

import java.util.Scanner;

public class Question_8 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the radius of the circle: ");
        double radius = input.nextDouble();

        double perimeter = 2 * Math.PI * radius;

        System.out.println(perimeter);



    }
}
