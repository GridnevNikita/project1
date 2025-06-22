# Задача 1
# Напишите функцию, которая принимает список дат в формате списка строк, например
# ["2022.12.31", "2023.1.7"]
# , и возвращает список дат в формате строк через одну неделю, например
# ["January 7, 2023", "January 14, 2023"]
import json
from datetime import datetime, timedelta


def reform_data(data):
    new_list = []
    for i in data:
        data_obj = datetime.strptime(i, '%Y.%m.%d')
        new_data_obj = data_obj + timedelta(days =7)
        new_list.append(new_data_obj.strftime('%B %#d, %Y'))
    return new_list


print(reform_data(["2022.12.31", "2023.1.7"]))



def days_amount(sata):
    new_sata = json.loads(sata)
    new_data = []
    for new in new_sata:
        start_date = datetime.strptime(new['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(new['end_date'], '%Y-%m-%d')
        duration = (end_date - start_date).days
        new_data.append(duration)
    return new_data


print(days_amount('''
[
    {
        "name": "Event 1",
        "start_date": "2022-01-01",
        "end_date": "2022-01-05"
    },
    {
        "name": "Event 2",
        "start_date": "2022-02-15",
        "end_date": "2022-02-18"
    },
    {
        "name": "Event 3",
        "start_date": "2022-03-10",
        "end_date": "2022-03-20"
    }
]
'''))


def get_days_between_dates(date1, date2):
    start_date = datetime.strptime(date1, '%d.%m.%Y')
    end_date = datetime.strptime(date2, "%d.%m.%Y")
    duration = (end_date - start_date).days
    return duration

print(get_days_between_dates("01.01.2022", "31.01.2022"))