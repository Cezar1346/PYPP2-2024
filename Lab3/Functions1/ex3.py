def solve(numheads, numlegs):
    for x in range(numheads + 1):
        y = numheads - x
        if 2*x +  4*y == numlegs:
            return x, y
    return False

chickens, rabbits = solve(35, 94)
print(f"chickens = {chickens}, rabbits = {rabbits}")