# except.ex.py

def try_f1():
    try:
        lst = [1,3,5,7,9]
        lst[5] # IndexError
    except:
        print("Error")

# try_f1()

def try_f2():
    try: # 특정상황이 있는 에러들은 위쪽에 배치하고 예외처리는 밑쪽에서
        value = int("10a") # valueError
    except ValueError as e:
        print("변환할 수 없습니다.")
    except Exception as e:
        print("Exception e:", e)
        print("type e:", type(e))


# try_f2()

def try_f3():

    result = 4 / 0 # ZeroDivisionError

# try_f3()

def example():
    num1 = input("첫 번째 숫자입력 : ")
    num2 = input("두 번째 숫자입력 : ")
   
    try:
    
        num1 = int(num1)
        num2 = int(num2) # integer 객체 생성
        result = num1 / num2

    except ValueError as e: # except 블록은 예외를 찾아서 처리해준다.
        print("정수형이 아니에요")
    except ZeroDivisionError as e:
        print("0으로 나눌 수 없어용")
    except Exception as e:
        print("e:", e)
    else: # 오류가 없을 때만 실행           
        print("{} / {} = {}".format(num1, num2, result))
    finally: # 오류와 상관없이 마지막에 실행 
        print("예외처리 완료")

#example()

# 특정경우에는 일부러 예외를 발생시키기도 합니다.
def beware_dog(animal):
    if animal == "dog":
        # 예외발생
        raise RuntimeError("멍멍") # 강제로 오류발생
    else:
        print("어서오슈")

try:
    beware_dog("cow")
    beware_dog("cat")
    beware_dog("dog")
except RuntimeError as e: # 알아두자! 이름을 변경하고자 할 때 as를 쓴다.
    print(e)
    print(type(e))

