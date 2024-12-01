SECRET_NUMBER = 7

user_input = int(input("enter a guess: "))

while(user_input != SECRET_NUMBER):
    if(user_input > SECRET_NUMBER):
        hint = f"{user_input} is TOO BIG"
    else:
        hint = f"{user_input} is TOO SMALL"

    print(hint)
    user_input = int(input("enter a guess: "))
print(f"Great guess! {user_input} is the secret number!")

