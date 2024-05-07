#include "User.h"

// Constructors
User::User(string setFirstName, string setLastName) {
	firstName = setFirstName;
	lastName = setLastName;
}

User::User(string setFirstName, string setLastName, string setWentworthID) {
	firstName = setFirstName;
	lastName = setLastName;
	wentworthID = setWentworthID;
}

// Method
void User::changeFirstName(string setFirstName) {
	cout << "New First Name Set from " << firstName;
	firstName = setFirstName;
	cout << " to " << firstName << endl;
}

void User::changeLastName(string setLastName) {
	cout << "New Last Name Set from " << lastName;
	lastName = setLastName;
	cout << " to " << lastName << endl;
}

void User::changeWentworthID(string setWentworthID) {
	cout << "New Wentworth ID Set from " << wentworthID;
	wentworthID = setWentworthID;
	cout << " to " << wentworthID << endl;
}

string User::showFirstName() {
	return firstName;
}

string User::showLastName() {
	return lastName;
}

string User::showWentworthID() {
	return wentworthID;
}

// Deconstructor
User::~User() {

}