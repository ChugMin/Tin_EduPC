x =  int(input("Nhập 1 số x: "))
y =  int(input("Nhập 1 số y: "))
sum = 0
for i in range(x, y +1):
    sum += i**2

print("Tổng các bình phương từ", x, "đến", y, "là:", sum)