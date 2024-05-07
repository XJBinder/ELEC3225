#pragma once
#include "User.h"

class Admin :
    public User
{
public:
    // Constructors
    Admin(string setFirstName, string setLastName);
    Admin(string setFirstName, string setLastName, string setWentworthID);

    // Methods
    void addCourse();
    void removeCourse();
    void addUser();
    void removeUser();
    void addStudentCourse();
    void removeStudentCourse();
    void searchRoster();
    void showRoster();

    // Deconstructor
    ~Admin();
};