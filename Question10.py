#Simple ATM Simulator
#User inputs
age = int(input("Enter Age:"))
day = input("Enter Day of the week: ").strip().upper()
num_tickets = int(input("Enter Number of tickets: "))
#Check condition for age to determine its category
if age < 3:
    base_price = 0
    category = "Toddler/Infant"
elif 3 <= age <= 12:
    base_price = 150
    category = "Child"
elif 13 <= age <= 59:
    base_price = 300
    category = "Adult"
else: # 60+
    base_price = 200
    category = "Senior"


weekend_days = ["Friday", "Saturday", "Sunday"]  #days which have discount
 #condition for checking days with discount
if day in weekend_days:
    discount_percent = 20
    discount_amount = base_price * 0.20
else:
    discount_percent = 0
    discount_amount = 0


price_after_discount = base_price - discount_amount #discounted prices
total_amount = price_after_discount * num_tickets  #Total 
#Display
print("\n=== TICKET DETAILS ===")
print(f"Category:        {category}")
print(f"Base Price:      ₹{base_price}")
if discount_percent > 0:
    print(f"Discount:        ₹{discount_amount:.2f} ({discount_percent}% Weekend Discount)")
else:
    print(f"Discount:        ₹0.00 (Weekday - No Discount)")

print(f"Price per ticket: ₹{price_after_discount:.2f}")
print("--------------------------")
print(f"Total Amount ({num_tickets} tickets): ₹{total_amount:.2f}")