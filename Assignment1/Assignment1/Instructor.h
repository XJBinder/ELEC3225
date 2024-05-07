#pragma once
#include "User.h"

class Instructor :
    public User
{
public:
    // Constructors
    Instructor(string setFirstName, string setLastName);
    Instructor(string setFirstName, string setLastName, string setWentworthID);

    // Methods
    void searchCourse();
    void showClassList();
    void showSchedule();

    // Deconstructor
    ~Instructor();
};