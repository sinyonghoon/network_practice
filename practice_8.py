def listProd(a, b):
    sum = 0
    for step in range(3):
        sum += a[step] * b[step]
    return sum
a = []
b = []
print("각 3개씩 입력해주십시오.")
for i in range(3):
    s = int(input("첫번재 리스트 {}번째 입력 : ".format(i+1)))
    a.append(s)
for i in range(3):
    s = int(input("두번째 리스트 {}번째 입력 : ".format(i + 1)))
    b.append(s)
# a = [10, 5, 3]
# b = [-1, 0, 4]
ans = listProd(a, b)
print("결과값은 {} 입니다.".format(ans))