def main():
    print("Simple cost calculator")
    expenses = []

    while True:
        entry = input("(Write here the amount of expenses) or to stop write 'stop'")
        if entry.lower() == 'stop':
            break

        try:
            amount = float(entry)
            expenses.append(amount)

        except ValueError:
            print("WRITE A NUMBER!")

        if expenses:
            total = sum(expenses)
            average = total/len(expenses)
            print(f"\nTotal {total: .2f} $")
            print(f"\nAverage {average: .2f} $")

        else:
            print("NO COST")

if __name__ == "__main__":
    main()