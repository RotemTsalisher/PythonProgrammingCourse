total_price = float(input("Please enter total price: "))

if(total_price >= 500):
    # apply 20 precent discount
    discount_applied = 20
elif(200 <= total_price <= 499):
    #apply 10 precent discount
    discount_applied = 10
else:
    discount_applied = 0
    # no discount

new_price = total_price*(1-discount_applied/100)
output_string = f"Discount: {discount_applied}%\nNew Price: {new_price}"
print(output_string)