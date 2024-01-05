from math import *

a = int(input("Nhập 1 số a bất kỳ: "))
b = int(input("Nhập 1 số b bất kỳ: "))
c = int(input("Nhập 1 số c bất kỳ: "))

s1 = ( -b + sqrt(b**2 - 4*a*c) ) / (2 * a)

s2 = (1 + c) * ( a + b / c ) / ( a - ( 1 / ( 1 + a**3 ) ) )

print(s1)
print(s2)

