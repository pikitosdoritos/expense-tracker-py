def main():
    print("Простой калькулятор расходов")
    expenses = []

    while True:
        entry = input("Введите сумму расхода (или 'стоп' для завершения): ")
        if entry.lower() == 'стоп':
            break
        try:
            amount = float(entry)
            expenses.append(amount)
        except ValueError:
            print("Пожалуйста, введите число!")

    if expenses:
        total = sum(expenses)
        average = total / len(expenses)
        print(f"\nИтоговая сумма расходов: {total:.2f} руб.")
        print(f"Средний расход: {average:.2f} руб.")
    else:
        print("Нет введённых расходов.")

if __name__ == "__main__":
    main()

