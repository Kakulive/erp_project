def print_menu(title, list_options):
    # """Prints options in standard menu format like this:

    # Main menu:
    # (1) Store manager
    # (2) Human resources manager
    # (3) Inventory manager
    # (0) Exit program

    # Args:
    #     title (str): the title of the menu (first row)
    #     list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    # """
    print(title)
    for i in range(1,len(list_options)):
        print(f"({i}) {list_options[i]}")
    print(f"({0}) {list_options[0]}")
    
def print_message(message):
    # """Prints a single message to the terminal.

    # Args:
    #     message: str - the message
    # """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    # """Prints tabular data like above.

    # Args:
    #     table: list of lists - the table to print out
    # """
    for i in table:
        print(i)

def get_input(label):
    # """Gets single string input from the user.

    # Args:
    #     label: str - the label before the user prompt
    # """
    new_input = input(f"{label}: ")
    return new_input

def get_inputs(labels):
    # """Gets a list of string inputs from the user.

    # Args:
    #     labels: list - the list of the labels to be displayed before each prompt
    # """
    inputs = []
    for i in range(len(labels)):
        new_input = input(f"{labels[i]}: ")
        inputs.append(new_input)
    return inputs

def print_error_message(message):
    # """Prints an error message to the terminal.

    # Args:
    #     message: str - the error message
    # """
    print(message)
