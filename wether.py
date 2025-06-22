import json


def get_avg_for_city(path, city):
    """Получение средней температуры за неделю"""
    try:
        with open(path) as f:
            try:
                city_data = json.load(f)
            except json.JSONDecoder:
                print('Ошибка декодирования файла')
                return False
    except FileNotFoundError:
        print('Файл не найден')
        return False

    avg_temp = round(sum(city_data[city].values()) / len(city_data[city].keys()), 2)
    out_data = {
        city: {
            "Average temperature": avg_temp
        }
    }
    with open('out.json', 'w') as out_file:
        json.dump(out_data, out_file, indent=4)


if __name__ == '__main__':
    get_avg_for_city('weather.json','Moscow')