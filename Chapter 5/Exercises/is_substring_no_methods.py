string = input("enter a string: ")
substring = input("enter a substring: ")

is_substring = False

for i in range(len(string) - len(substring) + 1):
    if(string[i:i+len(substring)] == substring):
        is_substring = True

if(is_substring == True):
    output = f"\"{substring}\" is a substring of \"{string}\""
else:
    output = f"\"{substring}\" is NOT a substring of \"{string}\""

print(output)
