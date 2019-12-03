def rep_cat(x):
    print (x)
  # Base case
	if x == 0:
    	return
  rec_cat (x - 1)  # A recursive call with a different argument
  print (x)


rec_cat (10)
