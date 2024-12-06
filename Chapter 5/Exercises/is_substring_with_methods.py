string = input("enter a string: ")
substring = input("enter a substring: ")

is_substring = (substring in string)

if(is_substring == True):
    output = f"\"{substring}\" is a substring of \"{string}\""
else:
    output = f"\"{substring}\" is NOT a substring of \"{string}\""

print(output)