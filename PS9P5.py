def total(qty, price):
  total = qty*price
  return total

qty = int(input("Enter quantity: "))
price = float(input("Enter price of each item: "))
totalbt = total(qty, price)
tax = totalbt*0.07
total = tax+totalbt

print("Total:", format(total, '.2f'))
print("Tax:", format(tax, '.2f'))
