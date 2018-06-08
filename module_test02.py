# module test02 

# from ... import

from math import pi, sin, cos, tan
from mymod import pi, add, subtract, divide # 모듈로 부터 메소드를 불러옴
# 메소드를 정의 안해도 되고, 객체생성도 필요없다

# 모듈명 지정없이 이름으로만 호출 할 수 있게한다
print(pi)

print(add(10,20))

# 객체 내부에 __module__ 을 확인하면 그 객체가 어느 모듈에 속해있는지 확인
# add 메서드의 모듈은 무엇인가

# print(add.__module__) # add의 모듈을 확인
#print(dir(add.__module__)) # add 메서드의 객체 내부변수와 객체의 목록 

# add 객체의 모듈에 있는 substract 함수를 실행해 봅시다
# eval : 문자열로 넘겨받은 내용에 대해 실행을 해준다.

print(eval(add.__module__+"substract(10,10)"))
