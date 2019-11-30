# # Inputs
PRICE = 500
# # Process
DISCOUNT30 = 0.3
DISCOUNT20 = 0.2
DISCOUNT10 = 0.1
DISCOUNT5 = 0.05
DISCOUNT0 = 0
DISCOUNT0 = 0
NEWPRICE = 0

if price >= 300:
    descuento = price * discount30
    newprice = price - descuento
    print("discount= ", discount30)
    print("price = ", newprice)
elif price >= 200 and price < 300:
    descuento = price * discount20
    newprice = price - descuento
    print("discount= ", discount20)
    print("price = ", newprice)
elif price >= 100 and price < 200:
    descuento = price * discount10
    newprice = price - descuento
    print("discount= ", discount10)
    print("price = ", newprice)
elif price < 100 and price >= 0:
    descuento = price * discount5
    newprice = price - descuento
    print("discount= ", discount5)
    print("price = ", newprice)
elif price < 0:
    descuento = price * discount0
    newprice = price
    print("No Discount")
    print("price = ", newprice)
