def main():
    print("Simple cost calculator")
    expenses = []

    while True:
        entry = input("(Enter the cost amount) or 'q' to finish: ")
        
        if entry.lower()=='q':
            break

        try:
            amount = float(entry)
            expenses.append(amount)

        except ValueError:
            print("Write the amount")

    if expenses:
        total = sum(expenses)
        average = total/len(expenses)
        print(f"Total {total: .2f} $")
        print(f"Average {average: .2f} $")

    else: 
        print("Sorry, sn error occurred")

if __name__ == "__main__":
    main()