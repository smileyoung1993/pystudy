# 조거눈 if ~ elif ~ else

n = -2

if n > 0:
    print("양수")
elif n < 0:
    print("음수")
else:
    print("0")

# if 는 중첩해서 사용할 수 있다.

# 루프를 3번이상 중첩했을 경우는 잘못 설정했을 경우다.
# 조건이 여러개일 경우는 : and, or 등 논리 연산자를 이용해서 조건을 조합할 수 있다.

# 조건 표현식

# java , c 의 삼항연산과 비슷

money = 12000
print("by texi" if money >= 13000 else "by bus")

money = 0
print("by texi" if money >= 10000 else "by walk" if money == 0 else "by bus")
# 풀어서 다시 정의해보자


