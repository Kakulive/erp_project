from model.crm import crm
from view import terminal as view
from collections import Counter


ID_INDEX = 0
NAME_INDEX = 1
MAIL_INDEX = 2
SUBSCRIBED = 3
HEADERS_INDEX = 0
NO_HEADERS_INDEX = 1

def duplicate_id_check(table):
    is_duplicated = True
    while is_duplicated:
        check = 0
        new_id = crm.generated_id()
        for row in table:
            if new_id == row[ID_INDEX]:
                check += 1
        if check == 0:
            is_duplicated = False
    return new_id

def search_id_check():
    table = crm.generate_crm_table()[NO_HEADERS_INDEX:]
    error_message = "Woah! There's no such user ID, try again!"
    valid_id = False
    while valid_id == False:
        user_id = view.get_input("Please select user ID")
        for i in range(len(table)):
            if table[i][ID_INDEX] == user_id:
                row_index = i
                valid_id = True
                break
        if valid_id == False:
            view.print_message(error_message)
    return row_index

def get_element_to_switch():
    error_message = "Woah! There's no such element, try again!"
    title = "Elements available for changing"
    options = ["name", "email", "subscribed"]
    view.print_input_menu(title, options)
    while True:
        title_of_element = view.get_input("Which Element would you like to switch?")
        if int(title_of_element) == 0:
            element_to_switch = NAME_INDEX
            break
        elif int(title_of_element) == 1:
            element_to_switch = MAIL_INDEX
            break
        elif int(title_of_element) == 2:
            element_to_switch = SUBSCRIBED
            break
        else:
            view.print_message(error_message)
    return element_to_switch

def list_customers():
    table = crm.generate_crm_table()
    view.print_table(table)


def add_customer():
    options = ["name", "email", "subscribed"]
    customer_input = view.get_inputs(options)
    table = crm.generate_crm_table()[NO_HEADERS_INDEX:]
    new_id = duplicate_id_check(table)
    customer_input.insert(0, new_id)
    table.append(customer_input)
    crm.overwrite_table(table)

def update_customer():
    table = crm.generate_crm_table()[NO_HEADERS_INDEX:]
    row_index = search_id_check()
    element_to_switch = get_element_to_switch()
    new_value = view.get_input("What's the new value")
    table[row_index][element_to_switch] = new_value
    crm.overwrite_table(table)


def delete_customer():
    table = crm.generate_crm_table()[NO_HEADERS_INDEX:]
    row_index = search_id_check()
    table.pop(row_index)
    crm.overwrite_table(table)

def get_subscribed_emails():
    table = crm.generate_crm_table()[NO_HEADERS_INDEX:]
    subscribed_mails = []
    for i in range(len(table)):
        if table[i][SUBSCRIBED] == str("1"):
            subscribed_mail = table[i][MAIL_INDEX]
            subscribed_mails.append(subscribed_mail)
    print(f'list of subscribed mails: {subscribed_mails}')

def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
