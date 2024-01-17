n  = int(input("Nhập n: "))
a = int(input("Nhập a: "))

t = 0
for i in range(0, n + 1):
    t += 1 / (a + i)
    
print("T =", t)