import jsn

def stat_decorator(func):
    """Декоратор для вывода статистики по отфильтрованным транзакциям."""

    def wrapper(*args, **kwargs):
        filtered_transactions = func(*args, **kwargs)
        total_amount = sum([transaction['amount'] for transaction in filtered_transactions])
        print(f"Отфильтровано {len(filtered_transactions)} транзакций на сумму {total_amount}")
        return filtered_transactions

    return wrapper

@stat_decorator
def filter_transactions_by_currency(input_file, output_file, currency):
    """Фильтрует транзакции по валюте и сохраняет результат в новый файл."""

    with open(input_file, 'r') as f:
        transactions = json.load(f)

    filtered_transactions = [transaction for transaction in transactions if transaction['currency'] == currency]

    with open(output_file, 'w') as f:
        json.dump(filtered_transactions, f, indent=4)

    return filtered_transactions

def main():
    input_file = 'transactions.json'
    output_file = 'transactions_filtered.json'
    currency = 'USD'

    filtered_transactions = filter_transactions_by_currency(input_file, output_file, currency)


if __name__ == '__main__':
    main()