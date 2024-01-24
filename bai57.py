from itertools import *
n =  int(input("Nhập 1 số n: "))

a = 1
b = 1
c = a + b
for i in count(start = 1):
    if a > n:
        break
    print(a, end = ' ')
    a = b
    b = c
    c = a + b
    
