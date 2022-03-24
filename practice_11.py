a = input("열고자 하는 파일의 이름을 입력하시오.")
accessMode = "r"
try :
    myFile = open(a, accessMode)
except FileNotFoundError:
    print("그런 파일은 존재하지않습니다.")
else:
    l = 1
    while True:
        line = myFile.readline()
        if not line: break
        print("{}: {}".format(l, line), end="")
        l += 1
    myFile.close()