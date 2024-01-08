n = int(input("Nhập vào 1 số có 2 chữ số bất kì: "))

dv = n % 10
n //= 10
chuc = n
flag= 12
if chuc == 1:
    print("Mười", end = ' ')
elif chuc == 2:
    print("Hai mươi", end = ' ')
elif chuc == 3:
    print("Ba mươi", end = ' ')
elif chuc == 4:
    print("Bốn mươi", end = ' ')
elif chuc == 5:
    print("Năm mươi", end = ' ')
elif chuc == 6:
    print("Sáu mươi", end = ' ')
elif chuc == 7:
    print("Bảy mươi", end = ' ')
elif chuc == 8:
    print("Tám mươi", end = ' ')
elif chuc == 9:
    print("Chín mươi", end = ' ')
else:
    flag = 0

if flag == 0:
    print("Nhập sai!")
else:
    if dv == 1:
        if chuc == 1:
            print("một")
        else:
            print('mốt')
    elif dv == 2:
        print("hai")
    elif dv == 3:
        print("ba")
    elif dv == 4:
        if chuc == 1:
            print("bốn")
        else:
            print("tư")
    elif dv == 5:
        print("lăm")
    elif dv == 6:
        print("sáu")
    elif dv == 7:
        print("bảy")
    elif dv == 8:
        print("tám")
    elif dv == 9:
        print("chín")
    elif dv == 0:
        print("")
    
