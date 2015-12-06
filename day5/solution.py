fd = open("data.txt","r")

alphabet = "abcdefghijklmnopqrstuvwxyz"
ctr = 0
for line in fd:
    
    vowel_count = 0

    line = line.strip()
    if "ab" in line:
        continue
    elif "cd" in line:
        continue
    elif "pq" in line:
        continue
    elif "xy" in line:
        continue
    
    for c in line:
        if "a" == c:
            vowel_count += 1
        if "e" == c:
            vowel_count += 1
        if "i" == c:
            vowel_count += 1
        if "o" == c:
            vowel_count += 1
        if "u" == c:
            vowel_count += 1

    if vowel_count < 3:
        continue

    for a in alphabet:
        if a*2 in line:
            ctr += 1
            break
    
print(ctr)



    
