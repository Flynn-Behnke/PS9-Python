def discount(price, drate, quant):
  totprice = float(price) * int(quant)
  damt = float(totprice) * float(drate) / 100
  dprice = float(totprice) - float(damt)
  return damt, dprice

price=float(input("Enter price of the item: "))
quant=int(input("Enter quantity: "))
drate=float(input("Enter discount rate as a percent: "))

damt,dprice = discount(price, drate, quant)

print("Discount amount:", damt, "Discounted price:", dprice)
