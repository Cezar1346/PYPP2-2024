list = list(map(int, input().split()))

mult = list[0]

for x in list:    
    mult = mult * x

print(mult)