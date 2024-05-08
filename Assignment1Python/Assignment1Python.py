# Referenced from Corey Schafer
# https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

class User:
    def __init__(self, firstName, lastName, wentworthID):
        self.firstName = firstName
        self.lastName = lastName
        self.wentworthID = wentworthID

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setWentworthID(self, wentworthID):
        self.wentworthID = wentworthID

    def showAllInfo(self):
        return 'First Name: {} Last Name: {} Wentworth ID: {}'.format(self.firstName, self.lastName, self.wentworthID)


class Student:
    def searchCourse(self, courseName):
        print('Course Name Method {}'.format(courseName))

    def addDropCourse(self, courseName):
        print('Add/Drop Course Method {}'.format(courseName))

    def showSchedule(self):
        print('Print Schedule Method')


class Instructor:
    def printSchedule(self):
        print('Print Schedule Method')

    def printClassList(self):
        print('Print Class List')

    def searchCourse(self, courseName):
        print('Course Name Method {}'.format(courseName))


class Admin:
    def addCourse(self, courseName):
        print('Add Course Method {}'.format(courseName))

    def removeCourse(self, courseName):
        print('Remove Course Method {}'.format(courseName))

    def addUser(self, firstName, lastName, wentworthID):
        print('Add User Method {} {} {}'.format(firstName, lastName, wentworthID))

    def removeUser(self, wentworthID):
        print('Remove User Method {}'.format(wentworthID))
    def addStudent(self, firstName, lastName, wentworthID):
        print('Add Student Method {} {} {}'.format(firstName, lastName, wentworthID))
    def removeStudent(self, wentworthID):
        print('Remove Student Method {}'.format(wentworthID))
    def searchRoster(self):
        print('Search Roster Method')
    def printRoster(self):
        print('Print Roster Method')
    def searchCourse(self, courseName):
        print('Search Course Method {}'.format(courseName))
    def printCourse(self):
        print('Print Course Method')


User = User('Jon', 'Binder', 'W00409648')
