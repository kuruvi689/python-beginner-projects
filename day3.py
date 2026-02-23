correct_pin = 1234
attempts = 0

correct_pin = "1234"
attempts = 0

while attempts < 3:
    entered = input("Enter your PIN: ")
    if entered.strip() == correct_pin:
        print("Access granted.")
        break
    else:
        print("Incorrect PIN. Try again.")
        attempts += 1
else:
    print("Too many failed attempts. Access denied.")
    exit()

balance = 10000
transactions = []
while True:
    print("\n--- mini banking system ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        print(f"Your current balance is: ${balance:.2f}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            transactions.append(("Deposit", amount))
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        maximum_withdrawal = 5000
        if amount > maximum_withdrawal:
            print(f"Amount exceeds the maximum withdrawal limit of ${maximum_withdrawal:.2f}. Please enter a lower amount.")
        elif 0 < amount <= balance:
            balance -= amount
            transactions.append(("Withdrawal", amount))
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Invalid amount. Please enter a positive number not exceeding your balance.")
    elif choice == '4':
        if not transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for i, (type_of_transaction, amount) in enumerate(transactions, start=1):
                print(f"{i}. {type_of_transaction}: ${amount:.2f}")
    elif choice == '5':
        print("Thank you for using the mini banking system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
