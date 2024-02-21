def specnums(n, m):
    for i in range(n, m):
        yield i ** 2

n = int(input())
m = int(input())
for num in specnums(n, m):
    print(num)