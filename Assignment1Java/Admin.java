package com.Assignment1Java;

public class Admin extends User {
    // Constructors
    public Admin(String setFirstName, String setLastName) {
        super(setFirstName, setLastName);
    }

    public Admin(String setFirstName, String setLastName, String setWentworthID) {
        super(setFirstName, setLastName, setWentworthID);
    }

    // Methods
    public void addCourse() {
        System.out.println("Admin Add Course Method");
    }

    public void removeCourse() {
        System.out.println("Admin Remove Course Method");
    }

    public void addUser() {
        System.out.println("Admin Add User Method");
    }

    public void removeUser() {
        System.out.println("Admin Remove User Method");
    }

    public void addStudentCourse() {
        System.out.println("Admin Add Student to Course Method");
    }

    public void removeStudentCourse() {
        System.out.println("Admin Remove Student from Course Method");
    }

    public void searchRoster() {
        System.out.println("Admin Search Roster Method");
    }

    public void showRoster() {
        System.out.println("Admin Print Roster Method");
    }

    public void searchCourse() {
        System.out.println("Admin Search Course Method");
    }

    public void showCourse() {
        System.out.println("Admin Show Course Method");
    }
}
