from math import *

a = int(input("Nhập vào 1 số nguyên: a = "))
b = int(input("Nhập vào 1 số nguyên: b = "))
c = int(input("Nhập vào 1 số nguyên: c = "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    tmp = -b / (2 * a)
    if (tmp == -0.0) :
        print("Phương trình có nghiệm kép: x1 = x2 =",0)
    else:
        print("Phương trình có nghiệm kép: x1 = x2 =", -b / (2 * a))
else:
    print("Phương trình có 2 nghiệm phân biệt:")
    x1 = ( -b + sqrt(b**2 - 4*a*c) ) / (2 * a)
    x2 = ( -b - sqrt(b**2 - 4*a*c) ) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
    
# Tests:
# 5 3 1
# -1 0 0
#  2 5 1
    