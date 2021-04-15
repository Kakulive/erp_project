from os import remove
from model.hr import hr
from view import terminal as view
from model import data_manager

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

def list_employees():
    table = hr.generate_employees_table()
    view.print_table(table)
    #view.print_error_message("Not implemented yet.")


def add_employee():
    options = ["Id", "Name", "Date of birth", "Department", "Clearance"]
    hr_input = view.get_inputs(hr.HEADERS)
    table = hr.generate_employees_table()
    
    new_id = duplicate_id_check(table)

    hr_input.insert(0, new_id)
    table.append(hr_input)
    hr.overwrite_table(table)
    #view.print_error_message("Not implemented yet.")


def update_employee():
    remove=['']
    hr_input = view.get_inputs_update(remove,"Enter Id value to update",'')
    hr_update = view.get_inputs_update(hr.HEADERS[1:],"Enter value to remove",hr.DATAFILE)
    table = hr.generate_employees_table()
    hr.update_employess_table(table,hr_input,hr_update,hr.DATAFILE)
 

    #view.print_error_message("Not implemented yet.")


def delete_employee():
    remove=['']
    hr_input = view.get_inputs_update(remove,"Enter Id,name value to remove this line",'')
    table = hr.generate_employees_table()
    hr.delete_employess_table(table,hr_input,hr.DATAFILE)


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


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
