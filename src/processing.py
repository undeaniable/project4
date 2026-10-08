def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словаерей по значению ключа 'state'."""

    filtered_list = []
    for item in data:
        if item.get('state') == state:
            filtered_list.append(item)

    return filtered_list


def get_date_from_item(item: dict) -> str:
    """Достает значение даты из словаря операции"""
    return item.get('date', '')


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словаерей по дате (ключ 'date')"""
    return sorted(data, key=get_date_from_item, reverse=reverse)


if __name__ == '__main__':
    test_data_for_filtering = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    print("Результат фильтрации:")
    print(filter_by_state(test_data_for_filtering))

    test_data_for_sorting = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    print("Результат сортировки:")
    print(sort_by_date(test_data_for_sorting))

