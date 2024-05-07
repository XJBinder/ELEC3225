#include <iostream>
#include "User.h"
#include "Student.h"
#include "Instructor.h"
#include "Admin.h"

using std::cout;

void main() {
	cout << "--Welcome to Leopard Web Class Registration--" << endl << endl;
	cout << "This is a test to show methods and classes work." << endl << endl;

	// Create Test Objects
	User Jon = User("Jon", "Binder", "W00409648");
	Student Carson = Student("Carson", "Mershon", "W00414243");
	Instructor Professor = Instructor("Douglas", "Dr. Dow");
	Admin Dave = Admin("Dave", "Doe");

	cout << "--Testing User Class--" << endl;

	// Testing all Methods of User class
	cout << Jon.showFirstName() << endl;
	cout << Jon.showLastName() << endl;
	cout << Jon.showWentworthID() << endl;
	Jon.changeFirstName("newTestFirstName");
	Jon.changeLastName("newTestLastName");
	Jon.changeWentworthID("newTestWentworthID");

	cout << endl << "--Testing Student Class--" << endl;

	// Testing all Methods of Student class
	cout << Carson.showFirstName() << endl;
	cout << Carson.showLastName() << endl;
	cout << Carson.showWentworthID() << endl;
	Carson.changeFirstName("CarsonNameChangeTest");
	Carson.changeLastName("MershonNameChangeTest");
	Carson.changeWentworthID("CarsonNewWentworthID");
	Carson.searchCourse();
	Carson.addDrop();
	Carson.showSchedule();

	cout << endl << "--Testing Instructor Class--" << endl;

	// Testing all Methods of Instructor class
	cout << Professor.showFirstName() << endl;
	cout << Professor.showLastName() << endl;
	Professor.changeFirstName("DouglasNameChangeTest");
	Professor.changeLastName("Dr. NameChangeTest");
	Professor.searchCourse();
	Professor.showClassList();
	Professor.showSchedule();

	cout << endl << "--Testing Admin Class--" << endl;

	// Testing all Methods of Admin class
	cout << Dave.showFirstName() << endl;
	cout << Dave.showLastName() << endl;
	Dave.changeFirstName("newAdminFirstName");
	Dave.changeLastName("newAdminLastName");
	Dave.addCourse();
	Dave.removeCourse();
	Dave.addUser();
	Dave.removeUser();
	Dave.addStudentCourse();
	Dave.removeStudentCourse();
	Dave.searchRoster();
	Dave.showRoster();
}