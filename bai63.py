def snt(n):
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
    return flag

n = int(input("Nhập vào 1 số n: "))
if (snt(n)):
    tong  = 0
    for i in range(1, n +1 ):
        if snt(i) == 1:
            print(i, end = ' ' )
            tong += i
    
    print("\nTổng của các số nguyên tố đó là:", tong)        
else:
    print(n, "không phải là số nguyên tố!")