# Task
# Given an integer,
# Given an integer, n, perform the following conditional actions:
# if n is odd, print Weird
# if n is even and in the inclusive range of 2 to 5 , print Not Weird
# if n is even and in the inclisive range of 6 to 20, print Weird
# if n is even and grater than 20, print Not Weird
def ifif(n):
    if (n % 2 != 0):
        print("Weird")
    elif (n % 2 == 0 and 2 <= n <= 5):
        print("Not Weird")
    elif(n % 2 == 0 and 6 <= n <= 20):
        print("Weird")
    elif(n % 2 == 0 and n > 20):
        print("Not Weird")


def main():
    n = int(input())
    ifif()


main()
