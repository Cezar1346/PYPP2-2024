ourlist = {
    "Dog" : 100,
    "Cat" : 50,
    "Elephant" : 2,
}

print(ourlist)

ourlist["Dog"] = 10
ourlist["Cat"] -= 20

for x in ourlist:
    print(x, ourlist[x])