package com.Assignment1Java;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int userInput;
        String newValue;

        System.out.println("--Welcome to Leopard Web Class Registration--\n");
        System.out.println("This is a test to show methods and classes work in Java.\n");

        // Create Test Objects
        User User = new User("Jon", "Binder", "W00409648");
        Student Student = new Student("Carson", "Mershon", "W00414141");
        Instructor Instructor = new Instructor("Douglas", "Dr. Dow");
        Admin Admin = new Admin("Dave", "Doe");

        System.out.println("--Test Objects--\n1) User");
        System.out.println("2) Student\n3) Instructor");
        System.out.println("4) Admin\n5) Exit\nWhich object would you like to test?");
        System.out.print(">> ");
        userInput = scanner.nextInt();

        while (userInput != 5) {
            switch (userInput) {
                // User was Selected
                case 1:
                    System.out.println("User " + User.showAllAttributes() + " was selected");
                    System.out.println("1) Change first name");
                    System.out.println("2) Change last name\n3) Change Wentworth ID\n>>");
                    userInput = scanner.nextInt();
                    switch (userInput) {
                        // Change First Name
                        case 1:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            User.changeFirstName(newValue);
                            break;
                        // Change Last Name
                        case 2:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            User.changeLastName(newValue);
                            break;
                        // Change Wentworth ID
                        case 3:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            User.changeWentworthID(newValue);
                            break;
                        default:
                            System.out.println("Invalid Input");
                            break;
                    }
                    break;
                // Student was Selected
                case 2:
                    System.out.println("Student " + Student.showAllAttributes() + " was selected");
                    System.out.println("\n1) Change first name");
                    System.out.println("2) Change last name\n3) Change Wentworth ID");
                    System.out.println("4) Search Course\n5) Add/Drop Course\n6) Print Schedule\n>>");
                    userInput = scanner.nextInt();
                    switch (userInput) {
                        // Change First Name
                        case 1:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            Student.changeFirstName(newValue);
                            break;
                        // Change Last Name
                        case 2:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            Student.changeLastName(newValue);
                            break;
                        // Change Wentworth ID
                        case 3:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            Student.changeWentworthID(newValue);
                            break;
                        // Search Course
                        case 4:
                            Student.searchCourse();
                            break;
                        // Add/Drop Course
                        case 5:
                            Student.addDrop();
                            break;
                        // Print Schedule
                        case 6:
                            Student.showSchedule();
                            break;
                        default:
                            System.out.println("Invalid Input");
                            break;
                    }
                    break;
                // Instructor was Selected
                case 3:
                    System.out.println("Instructor " + Instructor.showFirstName() + " " + Instructor.showLastName() + " was selected");
                    System.out.println("\n1) Change first name");
                    System.out.println("2) Change last name\n3) Search Course\n4) Print Class List");
                    System.out.println("5) Print Schedule\n>>");
                    userInput = scanner.nextInt();
                    switch (userInput) {
                        // Change First Name
                        case 1:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            Instructor.changeFirstName(newValue);
                            break;
                        // Change Last Name
                        case 2:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            Instructor.changeLastName(newValue);
                            break;
                        // Search for Course
                        case 3:
                            Instructor.searchCourse();
                            break;
                        // Print Class List
                        case 4:
                            Instructor.showClassList();
                            break;
                        // Print Schedule
                        case 5:
                            Instructor.showSchedule();
                            break;
                        default:
                            System.out.println("Invalid Input");
                            break;
                    }
                    break;
                // Admin was Selected
                case 4:
                    System.out.println("Admin " + Admin.showFirstName() + " " + Admin.showLastName() + " was selected");
                    System.out.println("\n1) Change first name");
                    System.out.println("2) Change last name\n3) Add Course\n4) Remove Course");
                    System.out.println("5) Add User\n6) Remove User\n7) Add Student Course");
                    System.out.println("8) Remove Student Course\n9) Search Roster\n10) Print Roster");
                    System.out.println("11) Search Course Method\n12) Show Course Method\n>>");
                    userInput = scanner.nextInt();
                    switch (userInput) {
                        // Change First Name
                        case 1:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            Admin.changeFirstName(newValue);
                            break;
                        // Change Last Name
                        case 2:
                            System.out.print(">> ");
                            newValue = scanner.next();
                            Admin.changeLastName(newValue);
                            break;
                        // Add Course
                        case 3:
                            Admin.addCourse();
                            break;
                        // Remove Course
                        case 4:
                            Admin.removeCourse();
                            break;
                        // Add User
                        case 5:
                            Admin.addUser();
                            break;
                        // Remove User
                        case 6:
                            Admin.removeUser();
                            break;
                        // Add Student Course
                        case 7:
                            Admin.addStudentCourse();
                            break;
                        // Remove Student Course
                        case 8:
                            Admin.removeStudentCourse();
                            break;
                        // Search Roster
                        case 9:
                            Admin.searchRoster();
                            break;
                        // Print Roster
                        case 10:
                            Admin.showRoster();
                            break;
                        // Search Course
                        case 11:
                            Admin.searchCourse();
                            break;
                        // Show Course
                        case 12:
                            Admin.showCourse();
                            break;
                        default:
                            System.out.println("Invalid Input");
                            break;
                    }
                    break;
                default:
                    System.out.println("Invalid Input");
                    break;
            }

            System.out.println("--Test Objects--\n1) User");
            System.out.println("2) Student\n3) Instructor");
            System.out.println("4) Admin\n5) Exit\nWhich object would you like to test?");
            System.out.print(">> ");
            userInput = scanner.nextInt();
        }
    }
}
