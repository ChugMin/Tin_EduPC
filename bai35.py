n  = int(input("Nhập n: "))

t = 0

for i in range(1, n + 1):
    t += (i - 1) / i

print("T =", t)