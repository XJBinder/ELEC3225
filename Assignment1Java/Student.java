package com.Assignment1Java;

public class Student extends User {
    // Constructor
    public Student(String setFirstName, String setLastName, String setWentworthID) {
        super(setFirstName, setLastName, setWentworthID);
    }

    // Methods
    public void searchCourse() {
        System.out.println("Student Searching Course Method");
    }

    public void addDrop() {
        System.out.println("Student Add/Drop Class Method");
    }

    public void showSchedule() {
        System.out.println("Student Print Schedule Method");
    }
}