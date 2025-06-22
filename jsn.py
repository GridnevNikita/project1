import requests
import json

def get_currency_rate(currency_code):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Failed to get currency rate")
    data = response.json()
    currency_data = data["Valute"].get(currency_code)
    if not currency_data:
        raise ValueError(f"No data for currency {currency_code}")
    return json.dumps({
        "currency_code": currency_code,
        "rate": currency_data["Value"],
    })

# Пример использования
if __name__ == "__main__":
    try:
        rate = get_currency_rate("RUB")
        print(rate)
        print(json.dumps(rate))
    except Exception as e:
        print(f"Ошибка: {e}")