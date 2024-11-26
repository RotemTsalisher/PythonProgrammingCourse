password = input("Please enter a password: ")
length = len(password)

if(length >= 8):
    # code here
    output_string = "Strong Password"
elif(5 <= length <=7):
    #code here
    output_string = "Medium Strength Passwords"
elif(0 < length < 5):
    #code here
    output_string = "Weak Password"
else:
    output_string = "Invalid Input"

print(output_string)
