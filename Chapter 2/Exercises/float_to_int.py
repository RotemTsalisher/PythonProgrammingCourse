float_number = float(input("enter a floating point number (two digits after decimal point): "))

# 13.34 -> int(13.34) = 13
whole_part = int(float_number)

# using the % operator:
#13.34 -> multiply by 100 -> int(1334) -> 1334 % 100 = 34
# 134 % 10 = 4
# 1345267 % 1000 = 267

fraction_part = int((float_number * 100) % 100)

print(f"float_number = {float_number:.2f}\nwhole_part = {whole_part}, fraction_part = {fraction_part}")
