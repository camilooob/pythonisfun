def maps():
    double_list = map(lambda i : i * 2, num_list)
    return (list(double_list))

def main():
    print(maps([0, 1, 2, 3, 4, 5]))

main()
