__author__ = 'rob00000'
#this program can accept 4 options.
#1. show all employees
#2. Add new employee
#3. delete existing
#4. find employee
#5. quit/exit program

# Bonus, read from a comma delemited file.

# input to the console

employee_db = {"Rob" : 39, "Amit" : 33, "Bruce" : 50, "Terry" : 51, "Harbie" : 29}

print employee_db["Rob"]

def show_all():
    print "show_all"
    print employee_db.items()

def add_employee():
    print "add_employee"
    name = raw_input("Enter New Employees Name: ")
    age = raw_input("Enter New Employees Age: ")
    new_employee = {name : age}
    employee_db.update(new_employee)

def delete_employee():
    print "delete_employee"
    name = raw_input("Enter Name of Employee You Would Like to Delete: ")
    if name.title() in employee_db:
        cert = raw_input("Are You Sure: Enter Y for Yes or N for No: ")
        if cert == "Y" or cert == "y":
            del employee_db[name.title()]
        else:
            print "You Selected No"
    else:
        print "Name is not in Datebase"

def find_employee():
    print "find_employee"
    name = raw_input("Enter Employee You Are Looking For: ")
    if name.title() in employee_db:
        print "this"
    else:
        print "Employee is not in database"


def exit():
    print "Exiting"


print "Welcome to Employee Database System"
while True:
    def menu_options():
        print "1. Show All Employees" + "\n" + "2. Add New Employee" + "\n" + "3. Delete Existing Employee" + "\n" + "4. Find Employees" + "\n" + "5. Exit Employee Database";
        selection = raw_input("Enter a number 1-5 ");
        return selection;

    user_selection = int(menu_options())

    print user_selection

    if user_selection == 1:
        show_all()

    elif user_selection == 2:
        add_employee()

    elif user_selection == 3:
        delete_employee()

    elif user_selection == 4:
        find_employee()

    elif user_selection == 5:
        exit()
        break


