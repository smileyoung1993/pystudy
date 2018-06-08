
def write01():
    
    # 텍스트 파일 쓰기
    f = open('./sample/test.txt','w', encoding="utf-8")
    size = f.write("Life is too short, you need Python") # 내용을 쓰고 길이를 반환
    print("write size: {} ".format(size))
    f.close() #열었으면 꼭 닫자


# write01()

def read01():
    # 텍스트 파일 읽기
    f = open("./sample/test.txt",'r',encoding="utf-8") # 파일 읽어오기
    text = f.read() # 객체로 읽은 내용을 text에 저장한다.
    print(text)
    f.close()

#read01()

def write02():
    # 여러줄을 만들어 봅시다
    f = open("./sample/multilines.txt",'w',encoding="utf-8")
    for i in range(1,10):
        f.write("Line %d\n" % i) # 1~9 까지 만든 텍스트 파일에 쓰자.
    f.close()

# write02()

def read02():
    f= open("./sample/multilines.txt",'r',encoding="utf-8")# 파일이 클경우 메모리 전체가 올라가서 문제가 된다.
    text = f.read() # 라인단위로 끊어 읽자
    print(text)
    f.close()

# read02()

def read02_1():
    f = open("./sample/multilines.txt","r",encoding="utf-8")
    # 루프를 돌면서 한줄 씩 읽어오자
    while(True):
        line = f.readline() # 계속돌면서 한라인씩 받아온다 readline():한라인씩 읽어온다.
        if not line: # 읽어올 라인이 없으면
            break
        print(line) # 읽어온 라인을 출력
    f.close()

# read02_1()

def read02_2():
    f = open("./sample/multilines.txt","r", encoding = "utf-8")
    lines = f.readlines()  # 통째로 불러와서 리스트로 저장하기 때문에 파일이 크면 메모리공간에 무리가 있다.
    print(lines) # 리스트로 읽어와서 나온다. --> 특정인덱스값을 찾을 수 있음
    f.close()

# read02_2()

# 연습문제

'''
sample directory 안 csv
파일을 열고 각 줄을 dict 로 만들고 리스트에 저장해 
'''

def slamdunk():
    members = [] #파일안 내용을 넣을 빈 리스트 
    f = open("./sample/sangbuk.csv","r",encoding = "utf-8") #csv파일을 연다
    line = f.readline() 
    while True: # 무한반복
        line = f.readline() # 파일의 내용을 한줄씩 읽어온다.
        if not line: #더이상 읽어 올 라인이 없으면 반복문 탈출
            break
        line = line.strip().replace(" ","")# replace는 중간에 있는 공백문자 제거, strip은 문자열을 앞,뒤 공백제거
        info = line.split(",") # ,를 기준으로 자르고, info에 넣어준다.
        member = { "name": info[0], "number": info[1], "height": info[2], "position": info[3]
        } # dict - key값을 가지는 dict 초기화 info[] ==> value


        members.append(member) # 리스트에 member dict 원소를 넣어준다.
    print(members)

slamdunk()

# 바이너리 파일 다루기 모드 : b
def binfile():
    f_src = open("./sample/rose-flower.jpeg",'rb')# 바이너리 모드로 파일을 읽는 객체생성
    data = f_src.read() # 객체가 파일을 읽고 그 내용을 data에 저장
    f_src.close()

    f_dest = open("./sample/rose-flowr-copy.jpeg",'wb') # 카피할 파일의 객체생성
    f_dest.write(data) # 데이터에 저장된 내용을 쓴다. 복사과정
    f_dest.close()

# binfile()

def safe_file():
    # 파일은 open 하면 반드시 닫아줘야한다
    # with ~ as 를 이용하면 파이썬이 사용 후 닫아준다.
    with open('./smaple/multilines.txt','r') as f: #단순히 파일이 순차적일때 사용하면 좋음
        for line in f.readlines():
            print(line , end="")
    print()

    # f가 닫혀있는지 확인
    print(f.close())

safe_file()