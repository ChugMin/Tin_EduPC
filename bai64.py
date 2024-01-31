def gt(n):
    if n <= 1:
        return 1
    else:
        return n * gt(n - 1)

n = int(input("Nhập vào 1 số n: "))

e = 1
for i in range(1, n + 1):
    e += 1 / (gt(i))
print("e =", e)