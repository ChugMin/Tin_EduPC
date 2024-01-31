def gt(n):
    if n <= 1:
        return 1
    return n  * gt(n - 1)

x = float(input("Nhập vào số x : "))
n = int(input("Nhập vào sô n: "))
a = 0
for i in range(1, n + 1):
    a += i * (x ** (i + 1)) 

b = 0
for  i in range(1, n + 1):
    b  += gt(i) ** 2
print('A =', a)
print('B =', b)