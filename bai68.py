a = int(input("Nhập vào 1 số a: "))
b = int(input("Nhập vào 1 số b: "))
dem =0
for i in range(a, b):
    a += 0.003 * a
    dem += 1
print('Sau', dem, 'tháng thì người đó sẽ nhận được số tiền ít nhất là', b, 'đồng')