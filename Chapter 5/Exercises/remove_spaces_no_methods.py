user_input = input("enter a string: ")
output_string = ""

for char in user_input:
    if(char != " "):
        output_string += char

print(f"User Input: {user_input}\nOutput: {output_string}")