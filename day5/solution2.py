import collections

fd = open("data.txt","r")

ctr = 0
for line in fd:
    line = line.strip()
    if all((line[i] != line[i+2]) for i in range(len(line)-2) ):
        continue
    elif all( line.count(str(line[i]+line[i+1])) != 2 for i in range(len(line)-1) ):
        continue
    ctr += 1
print(ctr)



    
