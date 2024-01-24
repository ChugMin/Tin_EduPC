n =int(input("Nhập 1 số n: "))
S = 0
for i in range(1, n + 1):
    S += i * (i + 1)
    
print("Giá trị của biểu thức S là:", S)