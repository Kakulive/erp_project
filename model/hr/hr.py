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
def birthday(table):
    for row in table:
        splited_birth_date = row[DATE_OF_BIRTH_INDEX].split('-')
        if int(splited_birth_date[2]) in range(birthday[2],birthday[2]+14):
            if int(splited_birth_date[1]) in range(int(birthday[1],birthday[1]+1)):
                date_birthday = splited_birth_date
            date_birthday = splited_birth_date

    worker = []
    for row in table:
        if row[DATE_OF_BIRTH_INDEX] == '-'.join(date_birthday):
            worker.append(row[NAME_INDEX])
    
    return worker