# Corey Schafer's YouTube
# https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

# Creating User Class
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
        return 'Firstname:{} Lastname:{} Wentworth ID:{}'.format(self.firstName, self.lastName, self.wentworthID)


# Creating Student Class
class Student(User):
    def searchCourse(self):
        print('Student Search Course Method')

    def addDropCourse(self):
        print('Student Add/Drop Course Method')

    def showSchedule(self):
        print('Student Print Schedule Method')


# Creating Instructor Class
class Instructor(User):
    # Overwriting User Classes Wentworth ID Attribute
    def __init__(self, firstName, lastName, wentworthID=None):
        super().__init__(firstName, lastName, wentworthID)

        # Sets wentworthID to "N/A" if no wentworthID is given as parameter
        if wentworthID is None:
            self.wentworthID = 'N/A'

    def showSchedule(self):
        print('Instructor Print Schedule Method')

    def showClassList(self):
        print('Instructor Print Class List Method')

    def searchCourse(self):
        print('Instructor Search Course Method')


# Creating Admin Class
class Admin(User):
    # Overwriting User Classes Wentworth ID Attribute
    def __init__(self, firstName, lastName, wentworthID=None):
        super().__init__(firstName, lastName, wentworthID)

        # Sets wentworthID to "N/A" if no wentworthID is given as parameter
        if wentworthID is None:
            self.wentworthID = 'N/A'

    def addCourse(self):
        print('Admin Add Course Method')

    def removeCourse(self):
        print('Admin Remove Course Method')

    def addUser(self):
        print('Admin Add User Method')

    def removeUser(self):
        print('Admin Remove User Method')

    def addStudent(self):
        print('Admin Add Student Method')

    def removeStudent(self):
        print('Admin Remove Student Method')

    def searchRoster(self):
        print('Admin Search Roster Method')

    def showRoster(self):
        print('Admin Print Roster Method')

    def searchCourse(self):
        print('Admin Search Course Method')

    def showCourse(self):
        print('Admin Print Course Method')


# Creating Objects
userObject = User('Jon', 'Binder', 'W00409648')
studentObject = Student('Carson', 'Mershon', 'W00414141')
professorObject = Instructor('Douglas', 'Dr. Dow')
adminObject = Admin('Admin', 'Person')

# Testing Methods
print('')

# User Class Test
print(userObject.showAllInfo())
userObject.setFirstName('JonTest')
userObject.setLastName('BinderTest')
userObject.setWentworthID('W00409648Test')
print(userObject.showAllInfo())

print('')

# Student Class Test
print(studentObject.showAllInfo())
studentObject.setFirstName('CarsonTest')
studentObject.setLastName('MershonTest')
studentObject.setWentworthID('W00414141Test')
print(studentObject.showAllInfo())
studentObject.searchCourse()
studentObject.addDropCourse()
studentObject.showSchedule()

print('')

# Instructor Class Test
print(professorObject.showAllInfo())
professorObject.setFirstName('DouglasTest')
professorObject.setLastName('Dr. DowTest')
print(professorObject.showAllInfo())
professorObject.showSchedule()
professorObject.showClassList()
professorObject.searchCourse()

print('')

# Admin Class Test
print(adminObject.showAllInfo())
adminObject.setFirstName('AdminTest')
adminObject.setLastName('PersonTest')
print(adminObject.showAllInfo())
adminObject.addCourse()
adminObject.removeCourse()
adminObject.addUser()
adminObject.removeUser()
adminObject.addStudent()
adminObject.removeStudent()
adminObject.searchRoster()
adminObject.showRoster()
adminObject.searchCourse()
adminObject.showCourse()