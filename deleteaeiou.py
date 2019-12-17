def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

def main():
	print(disemvowel("This website is for losers LOL!"))


main()
