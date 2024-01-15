n = int(input("Nhập số n (n >= 1): "))

s= 1
for i in range(1, n +1):
    s *= i
print(n, "! = ", s, sep = '') # sep: khoảng cách giữa các chuỗi
