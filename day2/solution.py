def solve():
    total = 0

    fd = open("./data.txt","r")

    if not fd:
        print("Could not open data file")
        exit(0)
    
    for line in fd:
        dimensions = line.strip().split("x")
            
        if len(dimensions) != 3:
            print("Bad dimension format")
            exit(0)

        print dimensions

        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])

        side1 = length*width
        side2 = width*height 
        side3 = height*length

        side_list = [side1, side2, side3]
        side_list.sort()

        extra = side_list[0]

        area = 2*side1 + 2*side2 + 2*side3

        total = total + area + extra
    return total
                

if __name__=="__main__":
    print("The solution is: %d" % solve())
