def shh (n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return (sum == n)


n = int(input("Nhập số n: "))

for i in range(1, n):
    if shh(i):
        print(i, end = ' ')