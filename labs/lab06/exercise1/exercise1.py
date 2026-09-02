# Item information
coffee_name = "Coffee"
coffee_price = 3.50
coffee_qty = 2

muffin_name = "Muffin"
muffin_price = 2.10
muffin_qty = 3

water_name = "Water"
water_price = 1.05
water_qty = 4

# Calculate totals
coffee_total = coffee_price * coffee_qty
muffin_total = muffin_price * muffin_qty
water_total = water_price * water_qty

subtotal = coffee_total + muffin_total + water_total
tax = subtotal * 0.06
final_total = subtotal + tax

# Create receipt as a single string
receipt = (
    "========== RECEIPT ==========\n"
    "Item\t\tPrice\tQty\tTotal\n"
    f"{coffee_name}\t\t${coffee_price:.2f}\t{coffee_qty}\t${coffee_total:.2f}\n"
    f"{muffin_name}\t\t${muffin_price:.2f}\t{muffin_qty}\t${muffin_total:.2f}\n"
    f"{water_name}\t\t${water_price:.2f}\t{water_qty}\t${water_total:.2f}\n"
    "------------------------------\n"
    f"Subtotal\t\t\t${subtotal:.2f}\n"
    f"Tax (6%)\t\t\t${tax:.2f}\n"
    f"Total\t\t\t${final_total:.2f}\n"
    "=============================="
)

print(receipt)