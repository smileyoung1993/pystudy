# pickle.ex.py

# 피클 사용을 위해 pickle을 import

import pickle

# 피클로 객체저장
def pwrite_01():
    f = open("./sample/players.bin",'wb') # b mode
    data = { "baseball" : 9 } # key = baseball , value = 9
    pickle.dump(data,f)
    f.close()

#pwrite_01()


def pread01():
    f = open("./sample/players.bin",'rb') # b mode
    data = pickle.load(f) # 파일로부터 피클을 로드 , 알아서 변환해줘서 저장
    f.close()
    print(data, type(data))

pread01()


def pwrite02():
    # 복수의 객체 저장
    with open("./sample/players.bin","wb") as f: # 객체 생성
        pickle.dump({"baseball" : 9},f,1) # protocol 1
        pickle.dump({"basketball" : 5},f,2) # protocol 2
        pickle.dump({"soccer" : 11},f,pickle.HIGHEST_PROTOCOL) # protocol 1
        
pwrite02()
'''
def pread02():
    # 복수의 객체 읽기
    with open("./sample/players.bin","rb") as f:
        print(pickle.load(f)) # 이전에 저장했던 데이터를 불러옴
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))

pread02() # EOFError
'''
def pread03():
    # 복수의 객체 읽기
    with open("./sample/players.bin","rb") as f:
        data_lst = []
        while True:
            try:
                data = pickle.load(f) # 파일에서 데이터 로드
            except EOFError:
                break

            data_lst.append(data)
        
        print(data_lst) 

pread03()  


