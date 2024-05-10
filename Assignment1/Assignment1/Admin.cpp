#include "Admin.h"

// Constructors
Admin::Admin(string setFirstName, string setLastName) : User(setFirstName, setLastName) {

}

Admin::Admin(string setFirstName, string setLastName, string setWentworthID) : User(setFirstName, setLastName, setWentworthID) {

}

// Methods
void Admin::addCourse() {
	cout << "Add Course Method" << endl;
}

void Admin::removeCourse() {
	cout << "Remove Course Method" << endl;
}

void Admin::addUser() {
	cout << "Add User Method" << endl;
}

void Admin::removeUser() {
	cout << "Remove User Method" << endl;
}

void Admin::addStudentCourse() {
	cout << "Add Student to Course Method" << endl;
}

void Admin::removeStudentCourse() {
	cout << "Remove Student from Course Method" << endl;
}

void Admin::searchRoster() {
	cout << "Search Roster Method" << endl;
}

void Admin::showRoster() {
	cout << "Print Roster Method" << endl;
}

void Admin::searchCourse() {
	cout << "Search Course Method" << endl;
}

void Admin::showCourse() {
	cout << "Show Course Method" << endl;
}

// Deconstructor
Admin::~Admin() {

}