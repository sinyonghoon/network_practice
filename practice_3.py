def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac*i
    return fac

a = input("자연수를 입력하시오.")
a = int(a)
ans = factorial(a)

print("자연수의 팩토리얼은 {} 입니다.".format(ans))