n =  int(input("Nhập 1 số n: "))
s = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        s += i
print("Tổng các số lẻ từ 1 đến", n, "là:", s)