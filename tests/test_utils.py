from src import utils
import pytest


def test_operations_of_clients():
    assert utils.operations_of_clients()


def test_last_five_operations():
    assert utils.last_five_operations([{"id": "6", "date": "01.06.2023", "state": "EXECUTED"},
                                       {"id": "5", "date": "01.04.2023", "state": "EXECUTED"},
                                       {"id": "2", "date": "01.03.2023", "state": "EXECUTED"},
                                       {"id": "3", "date": "01.02.2023", "state": "EXECUTED"},
                                       {"id": "1", "date": "01.01.2023", "state": "EXECUTED"}])
