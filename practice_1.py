a = input("자연수를 입력하시오.")
a = int(a)
sum =0
for i in range(a+1):
    sum += i
print("자연수의 합은 {} 입니다.".format(sum))