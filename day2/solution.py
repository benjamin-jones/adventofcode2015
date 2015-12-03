def solve():
    total = 0
    bowtotal = 0
    fd = open("./data.txt","r")

    if not fd:
        print("Could not open data file")
        exit(0)
    
    for line in fd:
        dimensions = line.strip().split("x")
            
        if len(dimensions) != 3:
            print("Bad dimension format")
            exit(0)

        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])

        dimension_list = [length, width, height]
        dimension_list.sort()

        side1 = length*width
        side2 = width*height 
        side3 = height*length

        side_list = [side1, side2, side3]
        side_list.sort()

        extra = side_list[0]

        bowside1 = dimension_list[0]
        bowside2 = dimension_list[1]

        bow_length = 2*(bowside1+bowside2)
        bow_length = bow_length + (length*width*height)

        area = 2*side1 + 2*side2 + 2*side3

        total = total + area + extra
        bowtotal = bowtotal + bow_length
    return total, bowtotal
                

if __name__=="__main__":

    total, bowtotal = solve()
    print("The solution is: \n%d wrapping paper \n%d bow" % (total, bowtotal))
