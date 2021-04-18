from model.sales import sales
from view import terminal as view

ID_INDEX = 0
CUSTOMER_INDEX = 1
PRODUCT_INDEX = 2
PRICE_INDEX = 3
DATE_INDEX = 4
HEADERS_INDEX = 0
NO_HEADERS_INDEX = 1

def duplicate_id_check(table):
    is_duplicated = True
    while is_duplicated:
        check = 0
        new_id = sales.generated_id()
        for row in table:
            if new_id == row[ID_INDEX]:
                check += 1
        if check == 0:
            is_duplicated = False
    return new_id

def search_id_check():
    table = sales.generate_sales_table()[NO_HEADERS_INDEX:]
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
    options = ["Customer id", "Product" ,"Price", "Date"]
    view.print_input_menu(title, options)
    while True:
        title_of_element = view.get_input("Which Element would you like to switch?")
        if int(title_of_element) == 0:
            element_to_switch = CUSTOMER_INDEX
            break
        elif int(title_of_element) == 1:
            element_to_switch = PRODUCT_INDEX
            break
        elif int(title_of_element) == 2:
            element_to_switch = PRICE_INDEX
            break
        elif int(title_of_element) == 3:
            element_to_switch = DATE_INDEX
            break
        else:
            view.print_message(error_message)
    return element_to_switch

def get_valid_dates_list():
    year_index = 0
    month_index = 1
    day_index = 2
    table = sales.generate_sales_table()[NO_HEADERS_INDEX:]
    valid_date_table = []
    options = ["Date from", "Date up to"]
    dates_range = view.get_inputs(options)
    date_from = dates_range[0].split("-")
    date_up_to = dates_range[1].split("-")

    for transaction in table:
        transaction[DATE_INDEX] = transaction[DATE_INDEX].split("-")
    
    for transaction in table:
        if int(transaction[DATE_INDEX][year_index]) > int(date_from[year_index]) and int(transaction[DATE_INDEX][year_index]) < int(date_up_to[year_index]):
            valid_date_table.append(transaction)

        elif int(transaction[DATE_INDEX][year_index]) == int(date_from[year_index]):
            if int(transaction[DATE_INDEX][month_index]) > int(date_from[month_index]):
                valid_date_table.append(transaction)
            elif int(transaction[DATE_INDEX][month_index]) == int(date_from[month_index]):
                if int(transaction[DATE_INDEX][day_index]) >= int(date_from[day_index]):
                    valid_date_table.append(transaction)
                      
        elif int(transaction[DATE_INDEX][year_index]) == int(date_up_to[year_index]):
            if int(transaction[DATE_INDEX][month_index]) < int(date_up_to[month_index]):
                valid_date_table.append(transaction)
            elif int(transaction[DATE_INDEX][month_index]) == int(date_up_to[month_index]):
                if int(transaction[DATE_INDEX][day_index]) <= int(date_up_to[day_index]):
                    valid_date_table.append(transaction)        

    return valid_date_table

def list_transactions():
    table = sales.generate_sales_table()
    view.print_table(table)

def add_transaction():
    options = ["Customer id", "Product" ,"Price", "Date"]
    transaction_input = view.get_inputs(options)
    table = sales.generate_sales_table()[NO_HEADERS_INDEX:]
    
    new_id = duplicate_id_check(table)

    transaction_input.insert(0, new_id)
    table.append(transaction_input)
    sales.overwrite_table(table)

def update_transaction():
    table = sales.generate_sales_table()[NO_HEADERS_INDEX:]
    row_index = search_id_check()
    element_to_switch = get_element_to_switch()
    new_value = view.get_input("What's the new value")
    table[row_index][element_to_switch] = new_value
    sales.overwrite_table(table)

def delete_transaction():
    table = sales.generate_sales_table()[NO_HEADERS_INDEX:]
    row_index = search_id_check()
    table.pop(row_index)
    sales.overwrite_table(table)

def get_biggest_revenue_transaction():
    table = sales.generate_sales_table()
    revenue_checker = 0
    biggest_transaction = []
    for transaction in table[NO_HEADERS_INDEX:]:
        if float(transaction[PRICE_INDEX]) > revenue_checker:
            revenue_checker = float(transaction[PRICE_INDEX])
            biggest = transaction
    biggest_transaction.append(biggest)
    biggest_transaction.insert(0,table[HEADERS_INDEX])
    label = "The transaction with the biggest revenue is"
    view.print_general_results(biggest_transaction, label)

def get_biggest_revenue_product():
    table = sales.generate_sales_table()[NO_HEADERS_INDEX:]
    products = {}
    for transaction in table:
        if transaction[PRODUCT_INDEX] not in products:
            products[transaction[PRODUCT_INDEX]] = float(transaction[PRICE_INDEX])
        else:
            products[transaction[PRODUCT_INDEX]] += float(transaction[PRICE_INDEX])
 
    max_revenue_product = max(products, key=products.get)

    label = "The biggest revenue product is"
    view.print_general_results(max_revenue_product, label)

def count_transactions_between():
    table = sales.generate_sales_table()[NO_HEADERS_INDEX:]
    valid_dates_table = get_valid_dates_list()

    label = "The amount of transactions between given dates is"
    view.print_general_results(len(valid_dates_table), label)

def sum_transactions_between():
    table = sales.generate_sales_table()[NO_HEADERS_INDEX:]
    valid_dates_table = get_valid_dates_list()
    transaction_sum = 0
    for transaction in valid_dates_table:
        transaction_sum += float(transaction[PRICE_INDEX])
    
    label = "The total revenue between given dates is"
    view.print_general_results(transaction_sum,label)

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
