#4000
#1h 6p 40s
#3600 360 40

num = int(input("Nhập vào 1 số nguyên bất kỳ: "))

gio = num // 3600
tmp = num  % 3600
phut = num % 360
giay = tmp // 60

print(gio, "giờ", phut, "phút", giay, "giây")