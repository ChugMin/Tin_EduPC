num = int(input("Nhập vào 1 số có 3 chữ số: "))

sum = num % 10
num //= 10
sum += num  % 10
num //= 10
sum += num % 10
num//= 10
sum += num

print("Tong cua cac chu so cua so do la:", sum)
