
n  = int(input("Nhập n: "))
flag = 1
dem = 1
if n <= 1:
    flag = 0
for i in range(2, n):
    if n % i == 0:
        dem+=1
    if dem > 1:
        flag = 0
        break

if flag == 1:
    print(n, "là số nguyên tố")
elif (flag == 0):
    print(n, "không là số nguyên tố")