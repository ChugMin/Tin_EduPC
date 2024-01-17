for i in range(10, 100):
    dv = i % 10
    chuc = i // 10
    if dv % 2 != 0 and chuc % 2 == 0: 
        print(i, end = ' ')