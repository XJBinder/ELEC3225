package com.Assignment1Java;

public class Instructor extends User {
    // Constructors
    public Instructor(String setFirstName, String setLastName) {
        super(setFirstName, setLastName);
    }

    public Instructor(String setFirstName, String setLastName, String setWentworthID) {
        super(setFirstName, setLastName, setWentworthID);
    }

    // Methods
    public void searchCourse() {
        System.out.println("Instructor Search Course Method");
    }

    public void showClassList() {
        System.out.println("Instructor Print Class List Method");
    }

    public void showSchedule() {
        System.out.println("Instructor Print Schedule Method");
    }
}
