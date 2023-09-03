from src.operation_class import Operation
import pytest as pytest


@pytest.fixture
def class_fixture_1():
    operation_test_1 = Operation({'date': '2000-12-08T22:46:21.935582',
                                  'operationAmount': {'amount': '41096.24',
                                                      'currency': {'name': 'USD', 'code': 'USD'}},
                                  'description': 'Открытие вклада',
                                  'to': 'Счет 90424923579946435907'})
    return operation_test_1


@pytest.fixture
def class_fixture_2():
    operation_test_2 = Operation({'date': '2018-07-31T12:25:32.579413',
                                  'operationAmount': {'amount': '34380.08',
                                                      'currency': {'name': 'USD', 'code': 'USD'}},
                                  'description': 'Перевод организации',
                                  'from': 'MasterCard 8532498887072395',
                                  'to': 'Счет 44238164562083919420'})
    return operation_test_2


def test___repr__(class_fixture_1):
    assert class_fixture_1.__repr__() == "Class Operation({'date': '2000-12-08T22:46:21.935582', " \
                                         "'operationAmount': {'amount': '41096.24', " \
                                         "'currency': {'name': 'USD', 'code': 'USD'}}, " \
                                         "'description': 'Открытие вклада', " \
                                         "'to': 'Счет 90424923579946435907'})"


def test_date(class_fixture_1):
    assert class_fixture_1.time() == "08.12.2000"


def test_description(class_fixture_1):
    assert class_fixture_1.description() == "Открытие вклада"


def test_account_from(class_fixture_1):
    assert class_fixture_1.from_somewhere() == ""


def test_account_from_2(class_fixture_2):
    assert class_fixture_2.from_somewhere() == "MasterCard 8532498887072395"


def test_account_to(class_fixture_1):
    assert class_fixture_1.to_somewhere() == "Счет 90424923579946435907"


def test_number_code(class_fixture_1):
    assert class_fixture_1.number_code(class_fixture_1.from_somewhere()) == "Внесение средств"


def test_number_code_1(class_fixture_1):
    assert class_fixture_1.number_code(class_fixture_1.to_somewhere()) == 'Счет **5907'


def test_number_code_2(class_fixture_2):
    assert class_fixture_2.number_code(class_fixture_2.to_somewhere()) == "Счет **9420"


def test_amount(class_fixture_1):
    assert class_fixture_1.amount() == "41096.24 USD"
