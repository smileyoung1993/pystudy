# in, not in : 포함관계를 나타내는 연산
# 리스트 내포도 같이 해 봅시다.
source = [x for x in range(1,100,2)] # 리스트 내포 # 앞의 x는 표현식 뒤의 x가 할당받고 앞의 x가 할당받은 값을 나타낸다.
# source에 다시 x 값을 할당해야 하므로 x 를 두번 쓴다.
print("source:",source)

if 2 in source:
    print("2를 포함하고 있습니다.")
else:
    print("2를 포함하고 있지 않습니다.")

# for : for ... in(객체)
for i in range(1 , 10 , 2):
    print(i,end=",")
else: # 루프가 종료없이 끝났을때
    print()

# 시퀀스 객체를 이용한 for문
animals = ['dog', 'cat', 'cow', 'tiger']
for animal in animals:
    print(animal,end=",")
else:
    print() # 루프가 끝났을 때 개행

# enumerate를 이용한 루프
for index, value in enumerate(animals): #튜플을 따로 분리할 필요없이 나눠져서 나온다.
    print(index, value)
    
# while
sum, i = 0,1

while i <= 100:
    sum += i
    i += 1

print("합계는: ", sum)