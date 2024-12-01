user_input = int(input("enter a positive integer: "))

while(user_input != 1):
    print(user_input)
    if(user_input % 2 == 0):
        user_input /= 2
    else:
        user_input = 3*user_input + 1

print(user_input)