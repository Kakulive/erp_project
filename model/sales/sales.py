""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]



def generated_id():
    new_id = util.generate_id()
    return new_id

def overwrite_table(table):
    data_manager.write_table_to_file(DATAFILE, table)
