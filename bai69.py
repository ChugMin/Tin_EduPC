dai = int(input("Nhập vào chiều dài: "))
rong = int(input("Nhập vào chiều rộng: "))

for i in range(rong):
    for j in range(dai):
        if i == 0 or i == rong - 1 or j == 0 or j == dai - 1:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()