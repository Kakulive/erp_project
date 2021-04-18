from model.hr import hr
from model import data_manager
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

def print_input_menu(title, list_options):
    print(title)
    for i in range(len(list_options)):
        print(f"({i}) {list_options[i]}")
    
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
    if isinstance(result, list) == True:
        print(f"{label}:")
        print_table(result)
    elif isinstance(result, tuple) == True:
        print(f"{label}: \n {result}")
    elif isinstance(result, dict) == True:
        print(f"{label}: \n {result}")
    elif isinstance(result, int) == True:
        print(f"{label}: {result}")
    elif isinstance(result, float) == True:
        print(f"{label}: {'%0.2f' % result}")
    else:
        print(f"{label}:")
        print(f"{result}")


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
    max_values = [0 for x in table[0]]
    for row in table:
        for index in range(len(row)):
            if max_values[index] < len(row[index]):
                max_values[index] = len(row[index])

    desired_empty_spaces = 3
    empty_spaces_on_sides = desired_empty_spaces*2
    max_values_expanded = [x+empty_spaces_on_sides for x in max_values]

    top_bar = f"/{(sum(max_values_expanded)+len(max_values_expanded)-1)*'-'}\ "
    bottom_bar = f"\{(sum(max_values_expanded)+len(max_values_expanded)-1)*'-'}/"

    print(top_bar)
    
    for i in range(len(table)-1):
        line = ''
        dashed_line = ''
        for j in range(len(table[i])):
            line += f"|{(max_values_expanded[j]-len(table[i][j]))//2*' '}{table[i][j]}{(max_values_expanded[j]-((max_values_expanded[j]-len(table[i][j]))//2)-len(table[i][j]))*' '}"
            dashed_line += f"|{max_values_expanded[j]*'-'}"
        line += "|"
        dashed_line += "|"
        print(line)
        print(dashed_line)
    
    last_table_line = ''
    for j in range(len(table[i])):
        last_table_line += f"|{(max_values_expanded[j]-len(table[-1][j]))//2*' '}{table[-1][j]}{(max_values_expanded[j]-((max_values_expanded[j]-len(table[-1][j]))//2)-len(table[-1][j]))*' '}"
    last_table_line += "|"
    print(last_table_line)

    print(bottom_bar)
    

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

def get_inputs_update(list_labels, title, file_list):
    print(title)
    answers = []
    for line in list_labels:
        if 'id' in line:
            a = (hr.generate_random(data_manager.get_table_from_file(file_list)))
            print('id:', a)
            answers.append(a)
        else:
            a = input(line)
            answers.append(a)
    return answers 