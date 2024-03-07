from time import sleep
import math

a = int(input())
b = int(input())

sqrt = math.sqrt(a)
mlsec = b/1000
sleep(mlsec)
print(sqrt)