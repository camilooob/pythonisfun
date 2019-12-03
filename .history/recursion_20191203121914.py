def rec_count (number):
  print (number)
  # Base case
  if number == 0:
    return 
  rec_count (number - 1)  # A recursive call with a different argument
  print (number)


rec_count (5)
