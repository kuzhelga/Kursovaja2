from utils import get_data, get_filtered_data, get_five_last_values, get_formated_data


def main():
    data = get_data()
    data = get_filtered_data(data)
    data = get_five_last_values(data)
    data = get_formated_data(data)

    for row in data:
        print(row)


if __name__ == '__main__':
    main()
