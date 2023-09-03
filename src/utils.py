import json
import os

data_path = os.path.abspath(r"C:\Users\pawlo\PycharmProjects\Course_work_3\data")
operations_path = os.path.join(data_path, "operation.json")


def operations_of_clients():
    with open(operations_path, "r", encoding='utf8') as file:
        operations_list = json.load(file)

        return operations_list


def last_five_operations(operations_list):
    clean_list = [op for op in operations_list if op != {} and op["state"] == "EXECUTED"]
    clean_list_sorted = sorted(clean_list, key=lambda dictionary: dictionary["date"], reverse=True)
    last_operations = clean_list_sorted[0:5]

    return last_operations
