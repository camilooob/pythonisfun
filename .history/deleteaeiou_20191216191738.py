def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

disemvowel("This website is for losers LOL!")
