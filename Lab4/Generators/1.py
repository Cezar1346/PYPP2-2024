def squaregenerator(n):
    for i in range(n):
        yield i*i

n = int(input())
for num in squaregenerator(n):
    print(num)