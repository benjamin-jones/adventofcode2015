from data import *

def solve():
    floor = 0
    for paren in parens:
        if paren == "(":
            floor = floor + 1
        else:
            floor = floor - 1
    return floor

if __name__=="__main__":
    print("The solution is %d" % solve())
