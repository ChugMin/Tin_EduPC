
n  = int(input("Nhập n: "))
m  = int(input("Nhập m (m > n): "))
sum = 0
for i in range(n, m + 1):
    if i % 3 == 0 or i % 5 == 0:
       sum += i
print("Tổng các số chia hết cho 3 hoặc 5 trong phạm vi từ", n, "đến", m, "là:", sum)