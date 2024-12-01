user_input = int(input("enter a non negative number (negative to stop): "))
sum = 0

while(user_input > -1):
    sum += user_input
    user_input = int(input("enter a non negative number (negative to stop): "))

print(f"sum = {sum}")