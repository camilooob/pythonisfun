def rec_count (number):
  print (number)
  # Base case
  if number == 5:
    return
  rec_count (number + 1)  # A recursive call with a different argument


rec_count (0)
