from hashlib import md5

inputval = "yzbqklnj"
i = 0
while True:
    test = inputval + str(i)
    digest = md5(test).hexdigest()
    if digest[0:5] == "00000":
        print(digest)
        print(i)
        break
    i = i + 1

i = 0
while True:
    test = inputval + str(i)
    digest = md5(test).hexdigest()
    if digest[0:6] == "000000":
        print(digest)
        print(i)
        break
    i = i + 1
