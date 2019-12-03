def rec_count (number):
  print (number)
  # Base case 
  rec_count (number - 1)  # A recursive call with a different argument
  print (number)


rec_count (5)
