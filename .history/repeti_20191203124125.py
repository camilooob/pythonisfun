def rec_cat (x):
  print (x)
  # Base case
  if x == x:
    return
  rec_cat (x)  # A recursive call with a different argument


rec_cat (5)
