def maps():
	double_list = map(lambda i : i * 2, num_list)
# This creates a new list. The original list remains unchanged.
	return (list(double_list))

def main():
	maps([0, 1, 2, 3, 4, 5])

main()
