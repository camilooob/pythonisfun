def main():
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

    elif PRICE >= 100 and PRICE < 200:
        DESCUENTO = PRICE * DISCOUNT10
        NEWPRICE = PRICE - DESCUENTO
        print("discount= ", DISCOUNT10)
        print("price = ", NEWPRICE)

    elif PRICE < 100 and PRICE >= 0:
        DESCUENTO = PRICE * DISCOUNT5
        NEWPRICE = PRICE - DESCUENTO
        print("discount= ", DISCOUNT5)
        print("price = ", NEWPRICE)

    elif PRICE < 0:
        DESCUENTO = PRICE * DISCOUNT0
        NEWPRICE = PRICE
        print("No Discount")
        print("price = ", NEWPRICE)


main()
