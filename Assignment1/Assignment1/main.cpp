#include <iostream>
#include "User.h"
#include "Student.h"
#include "Instructor.h"
#include "Admin.h"

int main() {
	int userInput;
	string newValue;

	cout << "--Welcome to Leopard Web Class Registration--" << endl << endl;
	cout << "This is a test to show methods and classes work in C++." << endl << endl;

	// Create Test Objects
	User Jon = User("Jon", "Binder", "W00409648");
	Student Carson = Student("Carson", "Mershon", "W00414243");
	Instructor Professor = Instructor("Douglas", "Dr. Dow");
	Admin Dave = Admin("Dave", "Doe");

	cout << "--Test Objects--" << endl << "1) Jon(User)" << endl;
	cout << "2) Carson(Student)" << endl << "3) Professor(Instructor)" << endl;
	cout << "4) Dave(Admin)" << endl << "5) Exit" << endl << "Which object would you like to test?" << endl;
	cout << ">>";
	cin >> userInput;

	while (userInput != 5) {
		switch (userInput) {
		// User Jon was Selected
		case 1:
			cout << "User " << Jon.showFirstName() << " " << Jon.showLastName() << " " << Jon.showWentworthID();
			cout << " was selected" << endl << "1) Change first name" << endl;
			cout << "2) Change last name" << endl << "3) Change Wentworth ID" << endl << ">>";
			cin >> userInput;
			switch (userInput) {
			// Change First Name
			case 1:
				cout << ">>";
				cin >> newValue;
				Jon.changeFirstName(newValue);
				break;
			// Change Last Name
			case 2:
				cout << ">>";
				cin >> newValue;
				Jon.changeLastName(newValue);
				break;
			// Change Wentworth ID
			case 3:
				cout << ">>";
				cin >> newValue;
				Jon.changeWentworthID(newValue);
				break;
			default:
				cout << "Invalid Input" << endl;
				break;
			}
			break;
		// Student Carson was Selected
		case 2:
			cout << "Student " << Carson.showFirstName() << " " << Carson.showLastName() << " " << Carson.showWentworthID();
			cout << " was selected" << endl << "1) Change first name" << endl << "2) Change last name" << endl;
			cout << "3) Change Wentworth ID" << endl << "4) Search Course" << endl << "5) Add/Drop Course" << endl;
			cout << "6) Print Schedule" << endl << ">>";
			cin >> userInput;
			switch (userInput) {
			// Change First Name
			case 1:
				cout << ">>";
				cin >> newValue;
				Carson.changeFirstName(newValue);
				break;
			// Change Last Name
			case 2:
				cout << ">>";
				cin >> newValue;
				Carson.changeLastName(newValue);
				break;
			// Change Wentworth ID
			case 3:
				cout << ">>";
				cin >> newValue;
				Carson.changeWentworthID(newValue);
				break;
			// Search Course
			case 4:
				Carson.searchCourse();
				break;
			// Add/Drop Course
			case 5:
				Carson.addDrop();
				break;
			// Print Schedule
			case 6:
				Carson.showSchedule();
				break;
			default:
				cout << "Invalid Input" << endl;
				break;
			}
			break;
		// Instructor Professor was Selected
		case 3:
			cout << "Instructor " << Professor.showFirstName() << " " << Professor.showLastName();
			cout << " was selected" << endl << "1) Change first name" << endl;
			cout << "2) Change last name" << endl << "3) Search Course" << endl << "4) Print Class List" << endl;
			cout << "5) Print Schedule" << endl << ">>";
			cin >> userInput;
			switch (userInput) {
			// Change First Name
			case 1:
				cout << ">>";
				cin >> newValue;
				Professor.changeFirstName(newValue);
				break;
			// Change Last Name
			case 2:
				cout << ">>";
				cin >> newValue;
				Professor.changeLastName(newValue);
				break;
			// Search for Course
			case 3:
				Professor.searchCourse();
				break;
			// Print Class List
			case 4:
				Professor.showClassList();
				break;
			// Print Schedule
			case 5:
				Professor.showSchedule();
				break;
			default:
				cout << "Invalid Input" << endl;
				break;
			}
			break;
		// Admin Dave was Selected
		case 4:
			cout << "Admin " << Dave.showFirstName() << " " << Dave.showLastName();
			cout << " was selected" << endl << "1) Change first name" << endl;
			cout << "2) Change last name" << endl << "3) Add Course" << endl << "4) Remove Course" << endl;
			cout << "5) Add User" << endl << "6) Remove User" << endl << "7) Add Student Course" << endl;
			cout << "8) Remove Student Course" << endl << "9) Search Roster" << endl << "10) Print Roster" << endl;
			cout << "11) Search Course Method" << endl << "12) Show Course Method" << endl << ">>";
			cin >> userInput;
			switch (userInput) {
			// Change First Name
			case 1:
				cout << ">>";
				cin >> newValue;
				Dave.changeFirstName(newValue);
				break;
			// Change Last Name
			case 2:
				cout << ">>";
				cin >> newValue;
				Dave.changeLastName(newValue);
				break;
			// Add Course
			case 3:
				Dave.addCourse();
				break;
			// Remove Course
			case 4:
				Dave.removeCourse();
				break;
			// Add User
			case 5:
				Dave.addUser();
				break;
			// Remove User
			case 6:
				Dave.removeUser();
				break;
			// Add Student Course
			case 7:
				Dave.addStudentCourse();
				break;
			// Remove Student Course
			case 8:
				Dave.removeStudentCourse();
				break;
			// Search Roster
			case 9:
				Dave.searchRoster();
				break;
			// Print Roster
			case 10:
				Dave.showRoster();
				break;
			// Search Course
			case 11:
				Dave.searchCourse();
				break;
			// Show Course
			case 12:
				Dave.showCourse();
				break;
			default:
				cout << "Invalid Input" << endl;
				break;
			}
			break;
		default:
			cout << "Invalid Input" << endl;
			break;
		}

		cout << "--Test Objects--" << endl << "1) Jon(User)" << endl;
		cout << "2) Carson(Student)" << endl << "3) Professor(Instructor)" << endl;
		cout << "4) Dave(Admin)" << endl << "5) Exit" << endl << "Which object would you like to test?" << endl;
		cout << ">>";
		cin >> userInput;
	}

	return 0;
}