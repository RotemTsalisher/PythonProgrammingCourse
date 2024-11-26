x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))

condition_met = (5 <= x <= 15) + (y % 3 == 0) + (z**2 > 50)

if(condition_met > 0):
    print(f"{condition_met} Conditions Met")
else:
    print("No Conditions Met")

#print(True + True + False + True) => 1 + 1 + 0 + 1