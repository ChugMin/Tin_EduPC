n = int(input("Nhập số n: "))

dem = 0
tbc = 0

for i in range(n, 0, -10):
    if i % 2 == 0 and i % 5 == 0:
       tbc += i
       dem+=1
print("Số lượng các số chia hết cho 2 và 5 là:", dem)
if dem == 0:
    print("Không có số nào chia hết cho 2 và 5!")
else:
    print("Trung bình cộng của các số đó là:", tbc / dem)