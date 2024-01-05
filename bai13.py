a = int(input("Nhập vào 1 số nguyên: a = "))
b = int(input("Nhập vào 1 số nguyên: b = "))

if (a == 0):
    if (b == 0) :
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    print("Phương trình có 1 nghiệm duy nhất: x =", -b  / a)
