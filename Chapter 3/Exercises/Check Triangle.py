a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if( (a + b > c) and (a + c > b) and (b + c > a) ):
    print("Valid Triangle!")
    if(a == b == c):
        print("Equilateral Triangle!")
    elif(a == b or a == c or b == c):
        print("Isosceles Triangle!")
    else:
        print("Scalene Triangle!")
else:
    print("Not a Valid Triangle!")
