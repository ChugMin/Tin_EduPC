from math import * 
def scp(n):
    tmp = int( sqrt(n))
    if tmp ** 2 == n:
        return True
    return False
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
    
# ý 1:
dem = 0
for  i in range(1, 100, 2):
    print(i, end = ' ')
    dem += 1
    if dem >= 11:
        break
print("\n")
# ý 2
dem = 0
n = 1
check = 1
cnt = 0
for i in range(1, 100):
    print(n, end = ' ')
    if cnt >= check:
        check += 1
        cnt = 0
    dem += 1
    if dem >= 11:
        break
    n  += check
    cnt  += 1
print("\n")
# ý 3
dem = 0
cnt = 1
n = 1
for i in range(1, 100):
    print(n, end = ' ')
    n += cnt
    if dem >= 11:
        break
    dem += 1
    cnt += 1
print("\n")
# ý 4
dem = 0
n = 1
cnt = 1
print(1, end = ' ')
for i in range(1, 10000):
    if scp(cnt) == 1:
        n += cnt
        print(n, end = ' ')
        dem += 1
    if dem >= 11:
        break
    cnt += 1
print("\n")
# ý 5:
dem = 0
cnt = 1
n = 1
for i in range(1, 100):
    print(n, end = ' ')
    n += cnt
    if dem >= 11:
        break
    dem += 1
    cnt += 2
print("\n")
# ý 6:
dem = 0
n = 1
cnt = 1
print(1, end = ' ')
for i in range(1, 10000):
    if snt(cnt) == 1:
        n += cnt
        print(n, end = ' ')
        dem += 1
    if dem >= 11:
        break
    cnt += 1
print("\n")
# ý 7:
dem = 0
cnt = 3
n = 1
for i in range(1, 100):
    print(n, end = ' ')
    n += cnt
    if dem >= 11:
        break
    dem += 1
    cnt += 2
print("\n")