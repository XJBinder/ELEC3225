#pragma once
#include <iostream>
#include <string>

using std::string;
using std::cin;
using std::cout;
using std::endl;

class User
{
	// Attribute
	string firstName, lastName, wentworthID;

public:
	// Constructors
	User(string setFirstName, string setLastName);
	User(string setFirstName, string setLastName, string setWentworthID);

	// Method
	void changeFirstName(string setFirstName);
	void changeLastName(string setLastName);
	void changeWentworthID(string setWentworthID);
	string showFirstName();
	string showLastName();
	string showWentworthID();

	// Deconstructor
	~User();
};