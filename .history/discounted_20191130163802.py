# # Inputs
PRICE = 500
# # Process
DISCOUNT30 = 0.3
DISCOUNT20 = 0.2
DISCOUNT10 = 0.1
DISCOUNT5 = 0.05
DISCOUNT0 = 0
DISCOUNTO = 0
NEWPRICE = 0

if PRICE >= 300:
    DESCUENTO = PRICE * DISCOUNT30
    NEWPRICE = PRICE - DESCUENTO
    print("discount= ", DISCOUNT30)
    print("price = ", NEWPRICE)
elif PRICE >= 200 and PRICE < 300:
    DESCUENTO = PRICE * DISCOUNT20
    NEWPRICE = PRICE - DESCUENTO
    print("discount= ", DISCOUNT20)
    print("price = ", NEWPRICE)
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
