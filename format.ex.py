# format.ex
#string format

'''
%s : string
%d : integer
%f : 부동소수
%% : %리터럴
'''

format = "i have %d apples"
print(format % 10)

print("i have %d apples" % 5)
print("Interest Rate is %.2f%%" % 1.24)

# 두개 이상의 값을 넣고 싶을 때
format = "total: %d개, get=%d개"
print(format % (10,3))

# format 과 값의 형식이 일치하지 않으면 타입에러가 발생

format_str = "I have {} apples, and i ate {} apples" # string formating

print(format_str.format(5,3))

# 서식에 설정된 공간의 개수와 실제 값의 개수가 다르면 인덱스 에러가 발생
print(format_str.format(10,3))  # over is okay
#print(format_str.format(10) # lack is occuring index error

# 이름 기반의 포맷
format_str = "I have {total} apples, and I ate {num} apples"
print(format_str.format(total = 10, num = 5))
#print(format_str.format(total = 10))# key error

#dict 객체를 이용한 포맷
print(format_str.format_map({"total": 5, "num": 2}))
# string format : seq end , format

