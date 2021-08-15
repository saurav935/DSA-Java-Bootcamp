
// Area of equilateral traingle

package com.company;

import java.util.Scanner;

public class Question_7 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the side of the equilateral triangle: ");

        double side = input.nextDouble();

        double area = (Math.sqrt(3) / 4) * (side * side);

        System.out.println(area);
    }
}
