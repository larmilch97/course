from src.utils import operations_of_clients, last_five_operations
from operation_class import Operation

# Загружаем список всех операций
operations_list = operations_of_clients()

# Создаем список из 5 последних выполненных операций
last_five_operations = last_five_operations(operations_list)

# Перебираем список и для каждой операции выводим данные
for element in last_five_operations:
    operation = Operation(element)
    print(f"""\n{operation.time()} {operation.description()}
    {operation.number_code(operation.from_somewhere())} -> {operation.number_code(operation.to_somewhere())}
    {operation.amount()}""")







