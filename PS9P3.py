def numbers(sales):
  if sales > 100000:
    com = 0.1*sales
  else:
    com = 0.05*sales

  target = 0.05*sales
  return com, target

name = str(input("Enter salesperson lastname: "))
sales = float(input("Enter sales: "))

com, target = numbers(sales)

print(name+"'s commision:", com, "and next year's target is:", target)
