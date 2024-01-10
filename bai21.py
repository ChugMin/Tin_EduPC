from math import *
r = int(input("Nhập vào 1 bán kính r = "))

x = int(input("Nhập vào tọa độ x: "))
y = int(input("Nhập vào tọa độ y: "))

d = sqrt(x**2 + y**2)
if d > r:
	print("Điểm A nằm ngoài đường tròn")
elif d == r:
	print("Điểm A nằm trên đường tròn")
else:
	print("Điểm A nằm trong đường tròn")