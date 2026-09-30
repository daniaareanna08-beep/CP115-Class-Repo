# Programmer : Dania Areanna
# Problem Description : Calculates and displays the amount of the bill to be paid after receiving the discount. 

# Prompt user for input
usage = float(input("Enter monthly usage amount (RM): "))

# Selection control structure to determine discount rate based on usage
if usage < 50:
    discount_rate = 0.00

elif usage <= 100:
    discount_rate = 0.05

else: 
    discount_rate = 0.20

# Calculate discount amount and total bill
discount_amount = usage * discount_rate
total_bill = usage - discount_amount

# Display output
print(f"Total amount due: RM{total_bill:.2f}")