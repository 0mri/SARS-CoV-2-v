import sqlite3
import sys
from persistence import *


def main(parameter_list):
    """
    Main function!
    """
    dbcon = sqlite3.connect('database.db')
    with dbcon:
        cursor = dbcon.cursor()
        # cursor.execute('DELETE Students')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS vaccines(id INTEGER PRIMARY KEY,date DATE NOT NULL,supplier INTEGER REFERENCES Supplier(id),quantity INTEGER NOT NULL)')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS logistics(id INTEGER PRIMARY KEY,name STRING NOT NULL,count_sent INTEGER NOT NULL,count_received, INTEGER NOT NULL)')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS suppliers(id INTEGER PRIMARY KEY,name STRING NOT NULL,logistic INTEGER REFERENCES logistics(id))')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS clinics (id INTEGER PRIMARY KEY,location STRING NOT NULL, demand INTEGER NOT NULL,logistic INTEGER REFERENCES logistic(id))')
        # cursor.execute('INSERT INTO Students Values(?, ?)', (1, 'Omri'))
        # cursor.execute('SELECT * FROM Students ')
        # students = cursor.fetchall()

    # print(students.)

    print(parameter_list)
    pass


if __name__ == "__main__":
    main(sys.argv[1:])
