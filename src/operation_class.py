import datetime


class Operation:
    def __init__(self, operation):
        self.operation = operation

    def __repr__(self):
        return f"Class Operation({self.operation})"

    def time(self):
        operation_date = self.operation["date"]
        operation_date_str = datetime.datetime.strptime(operation_date, "%Y-%m-%dT%H:%M:%S.%f")
        return operation_date_str.strftime("%d.%m.%Y")

    def description(self):
        return self.operation["description"]

    def from_somewhere(self):
        if "from" in self.operation.keys():
            return self.operation["from"]
        else:
            return ""

    def to_somewhere(self):
        return self.operation["to"]

    def number_code(self, account):
        if account == "":
            return "Внесение средств"
        else:
            account = account.split(" ")
            account_number = account[-1]
            account.pop(len(account) - 1)
            account_name = " ".join(account)
            if "Счет" in account:
                return f"{account_name} **{account_number[16:20]}"
            else:
                return f"{account_name} {account_number[0:4]} {account_number[4:6]}** **** {account_number[12:16]}"

    def amount(self):
        return f'{self.operation["operationAmount"]["amount"]} {self.operation["operationAmount"]["currency"]["name"]}'
