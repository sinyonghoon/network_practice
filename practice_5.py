a = input("온도를 입력하시오.")
b = input("섭씨로 변환이면 C를 화씨로 변환이면 F를 입력하시오.")
a = float(a)

if b == "F":
    tem = (9/5)*a+32
elif b == "C":
    tem = (5/9)*(a-32)
print("변환된 온도는 {} 입니다.".format(tem))