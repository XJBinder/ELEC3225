#pragma once
#include "User.h"

class Student :
    public User
{
public:
    // Constructor
    Student(string setFirstName, string setLastName, string setWentworthID);

    // Methods
    void searchCourse();
    void addDrop();
    void showSchedule();

    // Deconstructor
    ~Student();
};