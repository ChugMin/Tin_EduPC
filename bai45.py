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

n  = int(input("Nhập n: "))

for i in range(n, 0, -1):
    if snt(i) == 1:
        truoc = i
        break
for i in range(n, n + 100000000000000):
    if snt(i) == 1:
        sau = i
        break
print("2 số nguyên tố gần", n, "nhất là: (", truoc, ",", sau, ")")