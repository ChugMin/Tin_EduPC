n = int(input("Nhập vào 1 số nguyên bất kỳ: "))

if (n < 0):
	print(n, "là số âm")
elif ( n == 0 ):
	print(n, "là số không phải là số nguyên dương cũng không phải là số nguyên âm.")
else:
	print(n, "là số nguyên dương")
