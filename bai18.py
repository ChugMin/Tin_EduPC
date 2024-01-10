n = int(input("Nhập vào 1 số có 3 chữ số bất kì: "))

dv = n % 10
n //= 10
chuc = n % 10
n //= 10
tram = n
flag= 1

if tram == 1:
    print("Một trăm", end = ' ')
elif tram == 2:
    print("Hai trăm", end = ' ')
elif tram == 3:
    print("Ba trăm", end = ' ')
elif tram == 4:
    print("Bốn trăm", end = ' ')
elif tram == 5:
    print("Năm trăm", end = ' ')
elif tram == 6:
    print("Sáu trăm", end = ' ')
elif tram == 7:
    print("Bảy trăm", end = ' ')
elif tram == 8:
    print("Tám trăm", end = ' ')
elif tram == 9:
    print("Chín trăm", end = ' ')
else:
    flag = 0

if flag == 0:
    print("Nhập sai")
else:
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
    elif chuc == 0 and dv != 0:
        print('lẻ', end = ' ')
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
        if chuc == 0:
            print("năm")
        else:
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
