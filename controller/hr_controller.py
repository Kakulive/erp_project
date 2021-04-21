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
FUTURE = [1976, 11, 20]
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
    table = hr.generate_employees_table()[NO_HEADERS_INDEX:]
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
    table = hr.generate_employees_table()
    view.print_table(table)
    #view.print_error_message("Not implemented yet.")


def add_employee():
    options = [ "Name", "Date of birth", "Department", "Clearance"]
    transaction_input = view.get_inputs(options)
    table = hr.generate_employees_table()[NO_HEADERS_INDEX:]
    
    new_id = duplicate_id_check(table)

    transaction_input.insert(0, new_id)
    table.append(transaction_input)
    hr.overwrite_table(table)
    #view.print_error_message("Not implemented yet.")


def update_employee():
    table = hr.generate_employees_table()[NO_HEADERS_INDEX:]
    row_index = search_id_check()
    element_to_switch = get_element_to_switch()
    new_value = view.get_input("What's the new value")
    table[row_index][element_to_switch] = new_value
    hr.overwrite_table(table)
 

    #view.print_error_message("Not implemented yet.")


def delete_employee():
    table = hr.generate_employees_table()[NO_HEADERS_INDEX:]
    row_index = search_id_check()
    table.pop(row_index)
    hr.overwrite_table(table)



def get_oldest_and_youngest():
    # table = hr.generate_employees_table()[NO_HEADERS_INDEX:]
    # age = {}
    # for old_and_young in table:
    #     if old_and_young[NAME_INDEX] not in age:
    #         age[old_and_young[NAME_INDEX]] = int(age[DATE_OF_BIRTH_INDEX])
    #     else:
    #        age[old_and_young[NAME_INDEX]] += int(old_and_young[DATE_OF_BIRTH_INDEX])
 
    # max_age = max(age, key=age.get)

    # label = "The yanger person is"
    # view.print_general_results(max_age, label)
    
    # min_age = min(age, key=age.get)

    # label = "The oldest person is"
    # view.print_general_results(min_age, label)
    table = hr.generate_employees_table()[NO_HEADERS_INDEX:]
    label = "The oldest person: "
    result = hr.get_oldest_person(table)
    view.print_result(result, label)
    label = "The ounger person: "
    result = hr.get_yanger_person(table)
    view.print_result(result, label)

    
    
    
    

def get_average_age():
    table = hr.generate_employees_table()[NO_HEADERS_INDEX:]
    year = 2021
    average = 0
    count = 0
    
    for worker in table:
        splited_birth_date = worker[DATE_OF_BIRTH_INDEX].split('-')
        a = year - int(splited_birth_date[0])
        average = average + a 
        count +=1
    average = average / count
    label = "The average age is "
    view.print_general_results(average, label)
    


def next_birthdays():
    table = hr.generate_employees_table()[NO_HEADERS_INDEX:]
    label = "The birthday person: "
    result = hr.birthday(table)
    view.print_result(result, label)


def count_employees_with_clearance():
    
    table = hr.generate_employees_table()
    revenue_checker = 0
    biggest_clearance = []
    for clearance in table[NO_HEADERS_INDEX:]:
        if float(clearance[CLEARRANCE_INDEX]) > revenue_checker:
            revenue_checker = float(clearance[CLEARRANCE_INDEX])
            biggest = clearance
    biggest_clearance.append(biggest)
    biggest_clearance.insert(0,table[HEADERS_INDEX])
    label = "The clearance with the biggest revenue is"
    view.print_general_results(biggest_clearance, label)

def count_employees_per_department():
    tables = hr.generate_employees_table()[NO_HEADERS_INDEX:]
    genre = input("Chose the department")
    counter = 0
    for table in tables:
        if str(table[DEPARTMENT_INDEX]) == str(genre):
            counter += 1
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
