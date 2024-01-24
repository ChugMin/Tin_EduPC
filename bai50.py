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

n =  int(input("Nhập 1 số n: "))

dem = 1
for i in range(2, n + 1):
    if snt(i) == 1:
        print(i, end = ' ')
        if dem % 15 == 0:
            print()
        dem += 1