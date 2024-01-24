n =  input("Nhập 1 số n (hệ nhị phân): ")

l = len(n)
n = int(n)

kq = 0
dem = 0

for i in range(l):
    if n % 10 != 0:
        kq += (2 ** dem)

    dem += 1
    n //= 10
print("Kết quả:", kq)
    