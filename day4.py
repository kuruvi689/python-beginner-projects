while True:
    print("\nExpense Tracker Menu:")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total expenses")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        amount = input("Enter the expense amount: ")
        category = input("Enter the expense category: ")
        with open("Expense Tracker.txt", "a") as f:
            f.write(f"{amount} - {category}\n")
        print("Expense added successfully.")
    elif choice == '2':
        try:
            with open("Expense Tracker.txt", "r") as f_read:
                expenses = f_read.readlines()
                if not expenses:
                    print("No expenses recorded yet.")
                else:
                    print("All Expenses:")
                    for expense in expenses:
                        print(expense.strip())
        except FileNotFoundError:
            print("No expenses recorded yet.")
    elif choice == '3':
        total = 0
        try:
            with open("Expense Tracker.txt", "r") as f_read:
                expenses = f_read.readlines()
                for expense in expenses:
                    amount_str = expense.split('-')[0].strip()
                    try:
                        total += float(amount_str)
                    except ValueError:
                        pass
            print(f"Total Expenses: ${total:.2f}")
        except FileNotFoundError:
            print("No expenses recorded yet.")
    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")