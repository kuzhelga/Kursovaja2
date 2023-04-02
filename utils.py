import json
from pprint import pprint


def get_data():
    """Функция преобразует файл из формата json в python формат
    :return: data
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    """Функция фильтрует данные по статусу Исполнено (EXECUTED)
    """
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    return data

