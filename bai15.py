from math import *

a = int(input("Nhập vào 1 số a = "))
b = int(input("Nhập vào 1 số b = "))
c = int(input("Nhập vào 1 số c = "))

if a + b > c and b + c > a and  a + c > b:
    if a == b or b == c or a == c:
        if a == b and c == a:
            print("Tam giac nay la tam giac deu\n")
        else:
            print("Tam giac nay la tam giac can\n")
    else:
        print("Day la tam giac thuong\n")
    p = (a + b +c) / 2
    s = sqrt( p * (p - a) * (p - b) * (p - c) )
    print("Diện tích của tam giác đó là:", s)
else:
    print('3 cạnh trên không tạo thành 1 tam giác')