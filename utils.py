import json

def get_data():
    """Функция преобразует файл из формата json в python формат
    :return: data
    """
    with open ('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

