from model.sales import sales
from view import terminal as view

def duplicate_id_check(table):
    is_duplicated = True
    while is_duplicated:
        check = 0
        new_id = sales.generated_id()
        for row in table:
            if new_id == row[0]:
                check += 1
        if check == 0:
            is_duplicated = False
    return new_id

def list_transactions():
    table = sales.generate_sales_table()
    view.print_table(table)

def add_transaction():
    options = ["Customer id", "Product" ,"Price", "Date" ]
    transaction_input = view.get_inputs(options)
    table = sales.generate_sales_table()
    
    new_id = duplicate_id_check(table)

    transaction_input.insert(0, new_id)
    table.append(transaction_input)
    sales.overwrite_table(table)

def update_transaction():
    view.print_error_message("Not implemented yet.")


def delete_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
