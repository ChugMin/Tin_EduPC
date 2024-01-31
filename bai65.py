# bài 1:
for i in range(1, 100):
    for j in range(1, 100):
        if i * 2 + j * 4 == 100 and i + j == 36:
            print(i, ' ', j)
print('-----------------')
#bài 2:
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            if (i * 5 + j * 3 + (k / 3) == 100) and (i + j  + k == 100):
                print(i, ' ', j, ' ', ' ', k)