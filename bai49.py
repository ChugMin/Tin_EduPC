n =input("Nhập 1 số n: ")

d = len(n)
n = int(n)
s = 0
for i in range(d):
    s += n % 10
    n//=10

s += n
print("Tổng các chữ số của n:", s)