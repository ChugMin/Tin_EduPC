cha = int(input("Nhập tuổi của cha: "))
con = int(input("Nhập tuổi của con: "))

if cha > 2 * con and cha - con <= 25:
    print("Nhập tuổi sai!")
else:
    dem = 0
    for i in range(con, cha):
        if cha == 2 * con:
            break
        dem += 1
        con += 1
        cha += 1
    print(dem, "năm nữa thì tuổi cha gấp đôi tuổi con!")