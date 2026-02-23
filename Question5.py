#Bill Splitter
#User Entries
totalAmt=float(input("Enter total amount:"))
No_of_peaple=float(input("Enter No of customers:"))
tax=float(input("Enter tax percentage:"))
tip=float(input("Enter tip percentage:"))
#Display
print("=== BILL BREAKDOWN ===")
print("Subtotal:", totalAmt)
tax_amt = totalAmt * (tax/100)   #tax amount
print("Tax(", tax, "%) :", tax_amt)
after_tax = totalAmt + tax_amt #amount after tax is added
print("After tax:", after_tax)
tip_amt = after_tax * (tip/100) #tip amount
print("Tip(", tip, "%) :", tip_amt)
total = after_tax + tip_amt
print("Total:", total) #final total
print("Per Person:", total/4) #how much each person has to pay