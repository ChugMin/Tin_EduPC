def snt(n):
    flag = 1
    dem = 1
    if n <= 1:
        flag = 0
    for i in range(2, n):
        if n % i == 0:
            dem+=1
        if dem > 1:
            flag = 0
            break
    return flag

for i in range(3, 1000):
    if snt(i)  == 1 and snt(i + 2):
        print("(", i, ",", i + 2, ")")