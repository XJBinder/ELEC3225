#include "Student.h"

// Constructor
Student::Student(string setFirstName, string setLastName, string setWentworthID) : User(setFirstName, setLastName, setWentworthID) {
}

// Methods
void Student::searchCourse() {
	cout << "Searching Course Method" << endl;
}

void Student::addDrop() {
	cout << "Add/Drop Class Method" << endl;
}

void Student::showSchedule() {
	cout << "Print Schedule Method" << endl;
}

// Deconstructor
Student::~Student() {

}