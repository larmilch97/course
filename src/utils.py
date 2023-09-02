import json
import os

# Определяем путь к файлу данных в переменную

data_path = os.path.abspath("../data/")
operations_path = os.path.join(data_path, "operations.json")


def load_operations():
    """Загружает данные из файла и формирует список всех операций клиента """

    with open(operations_path, "r", encoding='utf8') as file:
        operations_list = json.load(file)

        return operations_list


def get_last_five_operations(operations_list):
    """Составляет отсортированный по дате список из 5 последних выполненных клиентом операций
    (без пустых и отклоненных операции)"""

    # clean_list = [op for op in operations_list if op != {} and op["state"] == "EXECUTED"]
    for op in operations_list:
        if op["state"] == "EXUCUTED":
            return op

    clean_list_sorted = sorted(op, key=lambda dictionary: dictionary["date"], reverse=True)
    last_five_operations = clean_list_sorted[0:5]

    return last_five_operations
