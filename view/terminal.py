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
    max_values = [0 for x in table[0]]
    for row in table:
        for index in range(len(row)):
            if max_values[index] < len(row[index]):
                max_values[index] = len(row[index])

    empty_spaces_on_sides = 3*2
    max_values_expanded = [x+empty_spaces_on_sides for x in max_values]

    top_bar = f"/{(sum(max_values_expanded)+len(max_values_expanded)-1)*'-'}\ "
    bottom_bar = f"\{(sum(max_values_expanded)+len(max_values_expanded)-1)*'-'}/"

    print(top_bar)
    
    for i in range(0,len(table)-1):
        line = f"|{(max_values_expanded[0]-len(table[i][0]))//2*' '}{table[i][0]}{(max_values_expanded[0]-((max_values_expanded[0]-len(table[i][0]))//2)-len(table[i][0]))*' '}|"\
        f"{(max_values_expanded[1]-len(table[i][1]))//2*' '}{table[i][1]}{(max_values_expanded[1]-((max_values_expanded[1]-len(table[i][1]))//2)-len(table[i][1]))*' '}|"\
        f"{(max_values_expanded[2]-len(table[i][2]))//2*' '}{table[i][2]}{(max_values_expanded[2]-((max_values_expanded[2]-len(table[i][2]))//2)-len(table[i][2]))*' '}|"\
        f"{(max_values_expanded[3]-len(table[i][3]))//2*' '}{table[i][3]}{(max_values_expanded[3]-((max_values_expanded[3]-len(table[i][3]))//2)-len(table[i][3]))*' '}|"\
        f"{(max_values_expanded[4]-len(table[i][4]))//2*' '}{table[i][4]}{(max_values_expanded[4]-((max_values_expanded[4]-len(table[i][4]))//2)-len(table[i][4]))*' '}|"
        dashed_line = f"|{max_values_expanded[0]*'-'}|{max_values_expanded[1]*'-'}|{max_values_expanded[2]*'-'}|{max_values_expanded[3]*'-'}|{max_values_expanded[4]*'-'}|"
        print(line)
        print(dashed_line)

    print(f"|{(max_values_expanded[0]-len(table[-1][0]))//2*' '}{table[-1][0]}{(max_values_expanded[0]-((max_values_expanded[0]-len(table[-1][0]))//2)-len(table[-1][0]))*' '}|"\
    f"{(max_values_expanded[1]-len(table[-1][1]))//2*' '}{table[-1][1]}{(max_values_expanded[1]-((max_values_expanded[1]-len(table[-1][1]))//2)-len(table[-1][1]))*' '}|"\
    f"{(max_values_expanded[2]-len(table[-1][2]))//2*' '}{table[-1][2]}{(max_values_expanded[2]-((max_values_expanded[2]-len(table[-1][2]))//2)-len(table[-1][2]))*' '}|"\
    f"{(max_values_expanded[3]-len(table[-1][3]))//2*' '}{table[-1][3]}{(max_values_expanded[3]-((max_values_expanded[3]-len(table[-1][3]))//2)-len(table[-1][3]))*' '}|"\
    f"{(max_values_expanded[4]-len(table[-1][4]))//2*' '}{table[-1][4]}{(max_values_expanded[4]-((max_values_expanded[4]-len(table[-1][4]))//2)-len(table[-1][4]))*' '}|")
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