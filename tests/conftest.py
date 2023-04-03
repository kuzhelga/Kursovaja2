import pytest

#we have 7 operations: with 6 state 'EXECUTED' and 5 with 'from'
@pytest.fixture

def test_data():
    return [{'id': 441945886, 'state': 'CANCELED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'},
            {'id': 414428826, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'NO': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'},
            {'id': 414253726, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'NO': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'},
            {'id': 414593826, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'},
            {'id': 125428826, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'},
            {'id': 125428826, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'}
            ]