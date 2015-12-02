from data import *

def solve():
    floor = 0
    position = 1
    final_position = 0
    for paren in parens:
        if paren == "(":
            floor = floor + 1
        else:
            floor = floor - 1
        if floor == -1 and final_position == 0:
            final_position = position
        position = position + 1
            
    return floor,final_position

if __name__=="__main__":
    floor, position = solve()
    print("The solution is %d %d" % (floor, position))
