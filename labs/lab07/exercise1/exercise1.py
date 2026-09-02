price1 = float(input())
quantity1 = int(input())
price2 = float(input())
quantity2 = int(input())
price3 = float(input())
quantity3 = int(input())
subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)
tax = subtotal * 0.06
total = subtotal + tax
print(subtotal)
print(tax)
print(total)
