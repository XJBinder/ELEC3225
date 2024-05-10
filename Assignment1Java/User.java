package com.Assignment1Java;

public class User {
    // Attributes
    private String firstName;
    private String lastName;
    private String wentworthID;

    // Constructors
    public User(String setFirstName, String setLastName) {
        this.firstName = setFirstName;
        this.lastName = setLastName;
    }

    public User(String setFirstName, String setLastName, String setWentworthID) {
        this.firstName = setFirstName;
        this.lastName = setLastName;
        this.wentworthID = setWentworthID;
    }

    // Methods
    public void changeFirstName(String setFirstName) {
        System.out.println("New First Name Set from " + this.firstName + " to " + setFirstName);
        this.firstName = setFirstName;
    }

    public void changeLastName(String setLastName) {
        System.out.println("New Last Name Set from " + this.lastName + " to " + setLastName);
        this.lastName = setLastName;
    }

    public void changeWentworthID(String setWentworthID) {
        System.out.println("New Wentworth ID Set from " + this.wentworthID + " to " + setWentworthID);
        this.wentworthID = setWentworthID;
    }

    public String showFirstName() {
        return this.firstName;
    }

    public String showLastName() {
        return this.lastName;
    }

    public String showWentworthID() {
        return this.wentworthID;
    }
    
    public String showAllAttributes() {
    	return this.firstName + " " + this.lastName + " " + this.wentworthID;
    }
}
