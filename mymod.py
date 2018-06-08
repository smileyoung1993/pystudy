# mymod.ex
# 내가 정의한 모듈


pi =3.14

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def main():
    print("mymod testcode")
    print("add", add(10,20))
    print("subtract", subtract(20,10))

if __name__ == "__main__":
    main()# 파이썬에서 바로 시작했을때 __main__출력
# import 했을때는 mymod가 출력
