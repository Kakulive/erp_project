""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
from view import terminal as view
import datetime
import calendar
ID_INDEX = 0
NAME_INDEX = 1
DATE_OF_BIRTH_INDEX = 2
DEPARTMENT_INDEX = 3
CLEARRANCE_INDEX = 4
HEADERS_INDEX = 0
NO_HEADERS_INDEX = 1
FUTURE = [1976, 11, 20]
FUTURE2 = [2020, 11, 20]
birthday = [2021,1,3]
DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def generate_employees_table():
    table = data_manager.read_table_from_file(DATAFILE)
    table.insert(0,HEADERS)
    return table
    
    
def generated_id():
    new_id = util.generate_id()
    return new_id

def overwrite_table(table):
    data_manager.write_table_to_file(DATAFILE, table)

def update_employess_table(table, id_, record, file_name):
    id_s = ''.join(id_)
    for line in table:
        if id_s in line:
            line[1:] = record 
            print('Update OK')          
        else:            
            pass
    data_manager.write_table_to_file(file_name, table)
    return record
  
def delete_employess_table(table, id_, file_name):
    for line in table:
        id_s = ''.join(id_)
        if id_s in line:
            table.remove(line)
            print('Remove OK')
        else:
            pass
    data_manager.write_table_to_file(file_name, table)
    return table

def get_oldest_person(table):
   
    oldest_birth_date = FUTURE2
    for row in table:
        splited_birth_date = row[DATE_OF_BIRTH_INDEX].split('-')
        if int(splited_birth_date[0]) <= int(oldest_birth_date[0]):
            if int(splited_birth_date[0]) == int(oldest_birth_date[0]) and int(splited_birth_date[1]) <= int(oldest_birth_date[1]):
                if int(splited_birth_date[1]) == int(oldest_birth_date[1]) and int(splited_birth_date[2]) <= int(oldest_birth_date[2]):
                    oldest_birth_date = splited_birth_date
                oldest_birth_date = splited_birth_date
            oldest_birth_date = splited_birth_date
                 
    oldest_persons = []
    for row in table:
        if row[DATE_OF_BIRTH_INDEX] == '-'.join(oldest_birth_date):
            oldest_persons.append(row[NAME_INDEX])
    
    return oldest_persons

def get_yanger_person(table):
       
    younger_birth_date = FUTURE
    for row in table:
        splited_birth_date = row[DATE_OF_BIRTH_INDEX].split('-')
        if int(splited_birth_date[0]) >= int(younger_birth_date[0]):
            if int(splited_birth_date[0]) == int(younger_birth_date[0]) and int(splited_birth_date[1]) <= int(oldest_birth_date[1]):
                if int(splited_birth_date[1]) == int(younger_birth_date[1]) and int(splited_birth_date[2]) <= int(oldest_birth_date[2]):
                   younger_birth_date = splited_birth_date
                younger_birth_date = splited_birth_date
            younger_birth_date = splited_birth_date
                 
    younger_persons = []
    for row in table:
        if row[DATE_OF_BIRTH_INDEX] == '-'.join(younger_birth_date):
            younger_persons.append(row[NAME_INDEX])
    
    return younger_persons
def average_age(table):
    
    year = 2021
    average = 0
    count = 0
    
    for worker in table:
        splited_birth_date = worker[DATE_OF_BIRTH_INDEX].split('-')
        a = year - int(splited_birth_date[0])
        average = average + a 
        count +=1
    average = average / count
    return average
def bigest_employees_with_clearance(table):

    check_level = view.get_input("Write level 1-7")
    biggest_clearance = []
    for clearance in table:
        if int(clearance[CLEARRANCE_INDEX]) >= int(check_level):
            biggest = clearance
            biggest_clearance.append(biggest)
    
    biggest_clearance.insert(0,HEADERS)
    return biggest_clearance

def department_count(table):
    genre = input("Chose the department")
    counter = 0
    for row in table:
        if str(row[DEPARTMENT_INDEX]) == str(genre):
            counter += 1
           
    return counter
def check_date_to_number(given_date):
    mounth = {"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}
    given_date = given_date.split("-")
    given_date_sum = 0
    for element in mounth.keys():
        if element == given_date[1]:
            break
        else:
            given_date_sum += mounth[element]
    given_date_sum += int(given_date[2])
    return given_date_sum
def birthday1(table):
    given_date = view.get_input("Write the date")
    name=[]
    date = []
    finally_list = []
    given_date = check_date_to_number(given_date)
    if given_date > 351:
        given_date_dec = (given_date + 14) % 365
    else:
        given_date_dec = given_date
    for row in table:
        name.append(row[NAME_INDEX])
        date_switch = check_date_to_number(row[DATE_OF_BIRTH_INDEX])
        date.append(date_switch)
    for index in range(len(date)):
        if (abs((date[index] - given_date)) < 14) or (abs((date[index] - given_date_dec)) < 14):
            finally_list.append(name[index])
    return finally_list


    