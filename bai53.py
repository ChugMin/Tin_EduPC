
n =  int(input("Nhập 1 số n: "))

kq = ""
for i in range(1, 1000):
    if (n <= 0):
        break
    du = str(n % 2)
    n //= 2

    kq = kq + du

kq = kq[::-1] # đảo chuỗi
print("Kết quả:", kq)