n = int(input("Nhập số n: "))
t = 0
for i in range(1, n + 1):
    t += 1 / i

print("Tổng các số là:", t)