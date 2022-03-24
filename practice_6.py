import math

a = input("반지름을 입력하시오.")
a = float(a)

ans1 = 4*math.pi*math.pow(a, 2)
ans2 = 4/3*math.pi*math.pow(a, 3)

print("겉면적은 {} 입니다.".format(ans1))
print("부피는 {} 입니다.".format(ans2))