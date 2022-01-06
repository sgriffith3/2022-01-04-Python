lcns = open("LICENSE", "r")
print(type(lcns))
lines = lcns.readlines()
print(lines)

txt = lcns.read()
print(txt)

lcns.read()


lcns.close()
