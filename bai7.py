num = int(input("Nhập vào 1 số có 2 chữ số: "))

sum = num % 10
num //= 10
sum += num

print("Tong cua cac chu so cua so do la:", sum)