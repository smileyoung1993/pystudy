# object.ex

print(id(3)) # id() is showing object address

# 변수에 3을 담는다
# 3객체를 만들고
# 변수에 3 객체의 id를 연결 심볼 테이블에 저장
a = 3
# a의 아이디 값을 확인해 봅시다
print("id a:",id(a))

b = 3 
print("id b:",id(b))

b = 4 
print("id b:",id(b))

# object simbol table

g_a = 2018
g_b = "simbol"

# global area           

def f(): # local area value
    l_a = "local"
    l_b = 5
    print(locals()) # local scope simbol table

print("----------: Local")
f()
print("----------: global")
print(globals())
print("f" in globals().keys())

# object copy
print("--------- object copy")

x= [1,2,3]
#{} = set format

# reference copy
y = x
print(x == y)
print(hex(id(x)),hex(id(y)))

x[1] = 4
print(y[1])

# try copy
y = x[:] # slicing copy
print("x",x)
print("y",y)

x[1] = 0
print(y[1])

# try copy : use copy module
import copy 
y= copy.copy(x)
print(x is y) # confirm ==
print("x:",x,"y:",y)

x[1] = 100
print("x:",x)
print("y:",y)

# deep copy
a = [1,2,3]
b = [4,5,a]
x = [a,b,100]

print("a:", a)
print("b:", b)
print("x:", x)

y = copy.copy(x)
print("y:", y)

a[1] = 0

print("a:", a)
print("b:", b)
print("x:", x)
print("y", y) # 객체는 카피가 됬지만 , 내부는 카피가 안된상황

# deep copy
print("======================")
y = copy.deepcopy(x)

print("a:", a)
print("b:", b)
print("x:", x)
print("y", y)

a[1] = 100
#y = copy.deepcopy(x)
print("x:", x)
print("y", y)
# deep copy는 객체를 다룰 때 편하다. ?????

