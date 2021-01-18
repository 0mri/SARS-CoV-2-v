
import sys
from persistence.Repository import repo
from persistence.DTO import *
from os import path

repo.create_tables()
if(not path.exists("database.db")):
    with open(sys.argv[1], 'r') as reader:
        line = reader.readline()
        data_arr = line.split(',')
        num_of_vaccines = int(data_arr[0])
        num_of_suppliers = int(data_arr[1])
        num_of_clinics = int(data_arr[2])
        num_of_logistics = int(data_arr[3])
        for vac in range(num_of_vaccines):
            cur_line = reader.readline()
            vaccine_data_arr = cur_line.split(',')
            vaccine = Vaccine(
                0, vaccine_data_arr[1], vaccine_data_arr[2], vaccine_data_arr[3])
            repo.vaccines.insert(vaccine)

        for sup in range(num_of_suppliers):
            cur_line = reader.readline()
            supplier_data_arr = cur_line.split(',')
            supplier = Supplier(
                supplier_data_arr[0], supplier_data_arr[1], supplier_data_arr[2])
            repo.suppliers.insert(supplier)

        for clinic in range(num_of_clinics):
            cur_line = reader.readline()
            clinic_data_arr = cur_line.split(',')
            clinic = Clinic(
                clinic_data_arr[0], clinic_data_arr[1], clinic_data_arr[2], clinic_data_arr[3])
            repo.clinics.insert(clinic)

        for log in range(num_of_logistics):
            cur_line = reader.readline()
            logistic_data_arr = cur_line.split(',')
            logistic = Logistic(
                logistic_data_arr[0], logistic_data_arr[1], logistic_data_arr[2], logistic_data_arr[3])
            repo.logistics.insert(logistic)

repo._conn.commit()


def output(parameter_list):
    """
    docstring
    """
    pass
