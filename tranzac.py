import jsn


def decorator_transaction(func):
    def wrapper(*args, **kwargs):
        filtered_transactions = func(*args, **kwargs)
        total_amount = sum([transaction['amount'] for transaction in filtered_transactions])
        print(f"Отфильтровано {len(filtered_transactions)} транзакций на сумму {total_amount}")
        return filtered_transactions

    return wrapper


@decorator_transaction
def filter_transactions_by_currency(input_file, output_file="transactions_filtered.json", currency="USD"):
    """Фильтрует транзакции по валюте и сохраняет результат в новый файл."""

    with open(input_file, 'r') as f:
        transactions = json.load(f)

    filtered_transactions = [transaction for transaction in transactions if transaction['currency'] == currency]

    with open(output_file, 'w') as f:
        json.dump(filtered_transactions, f, indent=4)

    return filtered_transactions


if __name__ == "__main__":
    filter_transactions_by_currency("transactions.json")
