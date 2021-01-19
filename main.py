import sqlite3
import sys
from persistence.Repository import repo
from persistence import *


def main(parameter_list):
    make_orders(order_path=parameter_list[1], output_path=parameter_list[2])


def make_orders(order_path, output_path):
    with open(order_path, 'r') as reader:
        for line in reader.readlines():
            order_data_arr = line.split(',')
            if len(order_data_arr) == 3:
                repo.receive(order_data_arr)
            if len(order_data_arr) == 2:
                repo.send(order_data_arr)
            output(output_path)


def output(path):
    result = [
        *repo.vaccines.sum(col="quantity"),
        *repo.clinics.sum(col="demand"),
        *repo.logistics.sum(col="count_received"),
        *repo.logistics.sum(col="count_sent")
    ]
    with open(path, "a") as writer:
        writer.write(','.join(map(str, result)) + '\n')


if __name__ == "__main__":
    main(sys.argv[1:])
