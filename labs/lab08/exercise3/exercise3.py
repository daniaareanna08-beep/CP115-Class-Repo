day_type = input()
show_time = int(input())
customer_type = input()

if day_type == "weekend":
    if customer_type == "Adult":
        base_price = 18
    elif customer_type == "Child":
        base_price = 12
    else: 
        base_price = 15

if day_type == "weekday":
    if customer_type == "Adult":
        base_price = 15
    elif customer_type == "Child":
        base_price = 10
    else: 
        base_price = 12

if show_time > 18:
    final_price = base_price + 3
else:
    final_price = base_price   
    
print(base_price)
print(final_price)
