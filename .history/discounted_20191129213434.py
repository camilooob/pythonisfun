# # Inputs
price = 100
# # Process
discount30 = 0.3
discount20 = 0.2
discount10 = 0.1
discount5 = 0.05
discount0 = 0
newprice

if price >= 300:
   newprice = price * discount30
   print(newprice)
else if price >= 200 and price > 300:
    newprice = price * discount20
    print(newprice)
else if price >= 100 and price > 200:
    newprice = price * discount10
    print(newprice)
else if price < 100 and price >= 0:
   newprice = price * discount5
   print(newprice)
else if price < 0:
    new price = price
    print(newprice)

