# Continuously ask the user for input until a valid number is provided
while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print("You entered a valid number:", number)
        break
    except ValueError:
        print("Invalid input, please enter a number.")
