h = int(input("Nhập vào chiều cao h: "))

for i in range(h):
    for j in range(h):
        if i >= j:
            print("*", end = ' ')
    print()

print()
for i in range(h):
    for j in range(h):
        if j <= h - i:
            print(end = ' ')
        else:
            print("*", end = ' ')
    print()
print()
for i in range(h):
    for j in range(h):
        if j >= i:
            print("*", end = ' ')
        if j < i:
            print(end = ' ')
    print()