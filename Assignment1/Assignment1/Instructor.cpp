#include "Instructor.h"

// Constructors
Instructor::Instructor(string setFirstName, string setLastName) : User(setFirstName, setLastName) {

}

Instructor::Instructor(string setFirstName, string setLastName, string setWentworthID) : User(setFirstName, setLastName, setWentworthID) {

}

// Methods
void Instructor::searchCourse() {
	cout << "Search Course Method" << endl;
}

void Instructor::showClassList() {
	cout << "Print Class List Method" << endl;
}

void Instructor::showSchedule() {
	cout << "Print Schedule Method" << endl;
}

// Deconstructor
Instructor::~Instructor() {

}