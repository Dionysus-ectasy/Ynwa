print("\nWelcome to Cedars Driving Federation!")
username_db = "Dangote"
password_db = "ipo@123"

user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")

if user_name == username_db and pass_word == password_db:
    print(f"Access granted. Welcome back to Cedars Driving Federation!")
    while True:
        print("\n---Driving Federation Menu:---")
        print("1. Check Driving License Status")
        print("2. Renew Driving License")
        print("3. Eligibility for New Driving License")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            print(f"Your driving license is valid and active.")
        elif choice == 2:
            print(f"Your driving license has been successfully renewed.")
        elif choice == 3:
            Age = int(input("Enter your age: "))
            if Age  >= 70:
                print(f"Attention, {user_name} You may need a medical examination to apply for a new driving license.")
            elif Age >= 18:
                print(f"Congratulations! {user_name} You are eligible to apply for a new driving license.")
            elif Age <= 17:
                print(f"Sorry, {user_name} You are not eligible to apply for a new driving license. You must be at least 18 years old.")
            elif Age < 0:
                print(f"Invalid age. Please enter a valid age.")
            else:
                print(f"Sorry, {user_name} You are not eligible to apply for a new driving license. You must be at least 18 years old.")
        elif choice == 4:
            print("Thank you for using Cedars Driving Federation. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid username or password.")