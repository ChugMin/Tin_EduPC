n = int(input("Nhập vào 1 năm bất kì: "))

if (n % 400 == 0) or  (n % 4 == 0 and n % 100 != 0):
    print('Năm', n, 'có 366 ngày')
else:
    print("Năm", n, 'có 365 ngày')