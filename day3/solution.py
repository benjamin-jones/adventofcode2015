from data import *

def solve():
    cached_locations = []
    santa_location = (0,0)
    robo_location = (0,0)
    cached_locations.append(santa_location)
    nHouses = 1

    player = 1

    for move in movements:
        if player == 1:
            x,y = santa_location 
        else:
            x,y = robo_location
        if move == ">":
            x = x + 1
        elif move == "<":
            x = x - 1
        elif move == "v":
            y = y - 1
        elif move == "^":
            y = y + 1
        if player == 1:
            santa_location = (x,y) 
        else: 
            robo_location = (x,y)

        if (x,y) not in cached_locations:
            nHouses = nHouses + 1
            cached_locations.append((x,y))
        player = -player

    

    return nHouses


if __name__=="__main__":
    result = solve()
    print(result)
