def get_user_input():
    while True:
        try : 
            user_input = input("Enter a number : ")
            number = int(user_input)
            return number
        except ValueError:
            print(f"Invalid input {user_input} in not a number. try Again !!")

number = get_user_input()
print("you have entered value : ",number)
