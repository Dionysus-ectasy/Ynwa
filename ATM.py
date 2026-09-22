print("\nWelcome to Sacrifice Bank ATM!")
print("Please insert your card.")
User_pin = int(input("Enter your PIN: "))
PIN = 2234

if User_pin == PIN:
    while True:
      print("\n---ATM Menu:---")
      print("Access granted. Please select a transaction.")
      print("1. Check Balance")
      print("2. Withdraw Cash")
      print("3. Deposit Cash")
      print("4. Exit")

      choice = int(input("Enter your choice (1-4): "))
      if choice == 1:
        print("Your balance is ₦100000.")
      elif choice == 2:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 100000:
            print(f"You have withdrawn ₦{amount}. Your new balance is ₦{100000 - amount}.")
        else:
            print("Insufficient balance.")
      elif choice == 3:
        amount = float(input("Enter the amount to deposit: "))
        print(f"You have deposited ₦{amount}. Your new balance is ₦{100000 + amount}.")
      elif choice == 4:
        print("Thank you for using Sacrifice Bank ATM. GoodBye!")
        break
      else:
        print("Invalid choice. Please try again.")
else:
    print("Access denied. Incorrect PIN.")