x  = int(input("Nhập x: "))
y  = int(input("Nhập y: "))

t = 1
for i in range(y):
   t *= x

print(x, "^", y, " = ", t, sep = '')