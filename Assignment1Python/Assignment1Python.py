# Corey Schafer's YouTube
# https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

# Creating User Class
class User:
    def __init__(self, first_name, last_name, wentworthID):
        self.first_name = first_name
        self.last_name = last_name
        self.wentworthID = wentworthID

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_wentworthID(self, wentworthID):
        self.wentworthID = wentworthID

    def show_all_info(self):
        return 'Firstname:{} Lastname:{} Wentworth ID:{}'.format(self.first_name, self.last_name, self.wentworthID)


# Creating Student Class
class Student(User):
    def search_course(self):
        print('Student Search Course Method')

    def add_drop_course(self):
        print('Student Add/Drop Course Method')

    def show_schedule(self):
        print('Student Print Schedule Method')


# Creating Instructor Class
class Instructor(User):
    # Overwriting User Classes Wentworth ID Attribute
    def __init__(self, first_name, last_name, wentworthID=None):
        super().__init__(first_name, last_name, wentworthID)

        # Sets wentworthID to "N/A" if no wentworthID is given as parameter
        if wentworthID is None:
            self.wentworthID = 'N/A'

    def show_schedule(self):
        print('Instructor Print Schedule Method')

    def show_class_list(self):
        print('Instructor Print Class List Method')

    def search_course(self):
        print('Instructor Search Course Method')


# Creating Admin Class
class Admin(User):
    # Overwriting User Classes Wentworth ID Attribute
    def __init__(self, first_name, last_name, wentworthID=None):
        super().__init__(first_name, last_name, wentworthID)

        # Sets wentworthID to "N/A" if no wentworthID is given as parameter
        if wentworthID is None:
            self.wentworthID = 'N/A'

    def add_course(self):
        print('Admin Add Course Method')

    def remove_course(self):
        print('Admin Remove Course Method')

    def add_user(self):
        print('Admin Add User Method')

    def remove_user(self):
        print('Admin Remove User Method')

    def add_student(self):
        print('Admin Add Student Method')

    def remove_student(self):
        print('Admin Remove Student Method')

    def search_roster(self):
        print('Admin Search Roster Method')

    def show_roster(self):
        print('Admin Print Roster Method')

    def search_course(self):
        print('Admin Search Course Method')

    def show_course(self):
        print('Admin Print Course Method')


# Creating Objects
user_object = User('Jon', 'Binder', 'W00409648')
student_object = Student('Carson', 'Mershon', 'W00414141')
professor_object = Instructor('Douglas', 'Dr. Dow')
admin_object = Admin('Admin', 'Person')

# Testing Methods
print('')

# User Class Test
print(user_object.show_all_info())
user_object.set_first_name('JonTest')
user_object.set_last_name('BinderTest')
user_object.set_wentworthID('W00409648Test')
print(user_object.show_all_info())

print('')

# Student Class Test
print(student_object.show_all_info())
student_object.set_first_name('CarsonTest')
student_object.set_last_name('MershonTest')
student_object.set_wentworthID('W00414141Test')
print(student_object.show_all_info())
student_object.search_course()
student_object.add_drop_course()
student_object.show_schedule()

print('')

# Instructor Class Test
print(professor_object.show_all_info())
professor_object.set_first_name('DouglasTest')
professor_object.set_last_name('Dr. DowTest')
print(professor_object.show_all_info())
professor_object.show_schedule()
professor_object.show_class_list()
professor_object.search_course()

print('')

# Admin Class Test
print(admin_object.show_all_info())
admin_object.set_first_name('AdminTest')
admin_object.set_last_name('PersonTest')
print(admin_object.show_all_info())
admin_object.add_course()
admin_object.remove_course()
admin_object.add_user()
admin_object.remove_user()
admin_object.add_student()
admin_object.remove_student()
admin_object.search_roster()
admin_object.show_roster()
admin_object.search_course()
admin_object.show_course()
