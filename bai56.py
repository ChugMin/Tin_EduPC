n =  int(input("Nhập 1 số n: "))

a = 1
b = 1
c = a + b
for i in range(n):
    print(a, end = ' ')
    a = b
    b = c
    c = a + b