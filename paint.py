# paint.py
# Point 클래스를 import
from point import Point
# 모듈명은 point
# import는 Point

p1 = Point(10,10)
print("p1",p1)
print("p1",repr(p1)) # 공식적인 문자열 출력# repr 메시지를 확인
print("instance_count: ",Point.instance_count)

p2 = Point(20,20)
print("p2",p2)
print("p2",repr(p2))# repr 메시지를 확인
print("instance_count: ",Point.instance_count)

p2_copy = eval(repr(p2))
print("p2_copy",p2_copy)