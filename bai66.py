n = int(input("Nhập vào số tiền bất kỳ (n % 10 == 0): "))
if n % 10 == 0:
    for i in range(0, n // 10 + 1):
        for j in range(0, n // 20 + 1):
            for k in range(0, n // 4  + 1):
                if i * 10 + j * 20 + k * 50 == n:
                    print(i, 'to 10 nghin', j, 'to 20 nghin', k, 'to 50 nghin')
else:
    print("Nhập sai!")