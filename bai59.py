a =  int(input("Nhập 1 số a: "))
b =  int(input("Nhập 1 số b: "))
le = 0
chan = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        le += i
    else:
        chan += i
print("Tổng các số lẻ giữa", a, 'và', b, 'là:', le)
print("Tổng các số chẵn giữa", a, 'và', b, 'là:', chan)