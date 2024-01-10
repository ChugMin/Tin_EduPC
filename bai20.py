month = int(input("Nhập vào 1 tháng bất kỳ trong năm: "))


if month == 2:
	year = int(input("Nhập vào 1 năm bất kỳ: "))
	if (year % 400 == 0) or  (year % 4 == 0 and year % 100 != 0):
		print("Tháng 2 có 29 ngày.")
	else:
		print("Tháng 2 có 28 ngày.")
elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
	print("Tháng", month, "có 31 ngày")
elif month == 4 or month == 6 or month == 9 or month == 11:
	print("Tháng", month, "có 30 ngày")
else:
	print("Nhập sai!")