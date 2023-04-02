import json
from datetime import datetime


def get_data():
    """Функция преобразует файл из формата json в python формат
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_filtered_data(data):
    """Функция фильтрует данные по статусу Исполнено (EXECUTED)
    """
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']

    return data


def get_data_with_from(data):
    """Функция фильтрует данные и возвращает по наличию поля 'from'
    """
    data = [x for x in data if 'from' in x]

    return data


def get_five_last_values(data):
    """Функция сортирует список по дате и возвращает последние 5 операций
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)

    return data[:5]


def get_formated_data(data):
    """ Функция с учетом типа счет/карта выводит данные по переводам в нужном формате
    """
    formated_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

        description = row['description']

        sender = row['from'].split()
        from_source = sender.pop(-1)
        if len(from_source) == 16:
            from_source = f'{from_source[:4]} {from_source[4:6]}** **** {from_source[-4:]}'
            from_info = ' '.join(sender)
        elif len(from_source) == 20:
            from_source = f'** {from_source[-4:]}'
            from_info = ' '.join(sender)
        else:
            print('this is not a card or account')

        recipient = row['to'].split()
        to_destination = recipient.pop(-1)
        if len(to_destination) == 16:
            to_destination = f'{to_destination[:4]} {to_destination[4:6]}** **** {to_destination[-4:]}'
            to_info = ' '.join(recipient)
        elif len(to_destination) == 20:
            to_destination = f'** {to_destination[-4:]}'
            to_info = ' '.join(recipient)
        else:
            print('this is not a card or account')

        formated_data.append(f"""
        {date} {description}
        {from_info} {from_source} -> {to_info} {to_destination}
        {row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}""")

    return formated_data
