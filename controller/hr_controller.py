from os import remove
from model.hr import hr
from view import terminal as view
from model import data_manager

ID_INDEX = 0
NAME_INDEX = 1
DATE_OF_BIRTH_INDEX = 2
DEPARTMENT_INDEX = 3
CLEARRANCE_INDEX = 4
HEADERS_INDEX = 0
NO_HEADERS_INDEX = 1

table = hr.generate_employees_table()[NO_HEADERS_INDEX:]
def duplicate_id_check(table):
    is_duplicated = True
    while is_duplicated:
        check = 0
        new_id = hr.generated_id()
        for row in table:
            if new_id == row[0]:
                check += 1
        if check == 0:
            is_duplicated = False
    return new_id
def search_id_check():
    error_message = "Woah! There's no such transaction, try again!"
    valid_id = False
    while valid_id == False:
        transaction_id = view.get_input("Please select transaction ID")
        for i in range(len(table)):
            if table[i][ID_INDEX] == transaction_id:
                row_index = i
                valid_id = True
                break
        if valid_id == False:
            view.print_message(error_message)
    return row_index
def get_element_to_switch():
    error_message = "Woah! There's no such element, try again!"
    title = "Elements available for changing"
    options = [ "Name", "Date of birth", "Department", "Clearance"]
    view.print_input_menu(title, options)
    while True:
        title_of_element = view.get_input("Which Element would you like to switch?")
        if int(title_of_element) == 0:
            element_to_switch = NAME_INDEX
            break
        elif int(title_of_element) == 1:
            element_to_switch = DATE_OF_BIRTH_INDEX
            break
        elif int(title_of_element) == 2:
            element_to_switch = DEPARTMENT_INDEX
            break
        elif int(title_of_element) == 3:
            element_to_switch = CLEARRANCE_INDEX
            break
        else:
            view.print_message(error_message)
    return element_to_switch


   
def list_employees():
    view.print_table(table)



def add_employee():
    options = [ "Name", "Date of birth", "Department", "Clearance"]
    transaction_input = view.get_inputs(options)
    
    new_id = duplicate_id_check(table)

    transaction_input.insert(0, new_id)
    table.append(transaction_input)
    hr.overwrite_table(table)


def update_employee():
    
    row_index = search_id_check()
    element_to_switch = get_element_to_switch()
    new_value = view.get_input("What's the new value")
    table[row_index][element_to_switch] = new_value
    hr.overwrite_table(table)


def delete_employee():
   
    row_index = search_id_check()
    table.pop(row_index)
    hr.overwrite_table(table)



def get_oldest_and_youngest():

    
    label = "The oldest person: "
    result = hr.get_oldest_person(table)
    view.print_result(result, label)
    label = "The ounger person: "
    result = hr.get_yanger_person(table)
    view.print_result(result, label)


def get_average_age():

   
    average = hr.average_age(table)
    label = "The average age is "
    view.print_general_results(average, label)
    


def next_birthdays():
    
    label = "The birthday person: "
    result = hr.birthday1(table)
    view.print_result(result, label)


def count_employees_with_clearance():
    
   
    biggest_clearance = hr.bigest_employees_with_clearance(table)
    label = "The clearance with the biggest revenue is"
    view.print_general_results(biggest_clearance, label)

def count_employees_per_department():
    
    counter = hr.department_count(table)
    label = "employees department  is"
    view.print_general_results(counter, label)


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
