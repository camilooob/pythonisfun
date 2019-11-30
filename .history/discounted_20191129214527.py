# # Inputs
price = 100
# # Process
discount30 = 0.3
discount20 = 0.2
discount10 = 0.1
discount5 = 0.05
discount0 = 0
descuento = 0
newprice = 0

if price >= 300:
   descuento = price * discount30
   print("discount= "discount30)
elif price >= 200 and price < 300:
    descuento = price * discount20
    newprice = price - descuento
    print("discount= "discount20)
    print("price = "newprice)
elif price >= 100 and price < 200:
    descuento = price * discount10
    newprice = price - descuento
    print("discount= "discount30)
	print("price = "newprice)
elif price < 100 and price >= 0:
   descuento = price * discount5
   newprice = price - descuento
   print("discount= "discount5)
   print("price = "newprice)
elif price < 0:
    descuento = price * discount0
    newprice = price
    print("No Discount")
    print("price = "newprice)

