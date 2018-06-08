# quiz01_3
# list와 dictionary
import math

students = [
    {   
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {   
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]

s_dic1 = {}
s_dic2 = {}

s_dic1['name'] = 'kim'
s_dic1['kor'] = 80
s_dic1['eng'] = 90
s_dic1['math'] = 80

s_dic1['total'] = s_dic1['kor'] + s_dic1['eng'] + s_dic1['math']
s_dic1['reverage'] = round((s_dic1['total'] / 3),1)


s_dic2['name'] = 'Lee'
s_dic2['kor'] = 90
s_dic2['eng'] = 85
s_dic2['math'] = 85

s_dic2['total'] = s_dic2['kor'] + s_dic2['eng'] + s_dic2['math']
s_dic2['reverage'] = round((s_dic2['total'] / 3),1)

print(s_dic1)

'''
s_lst1 = list(zip(s_dic1.keys(),s_dic1.values()))

for key, value in s_lst1:
    print("\"{}\" : {}".format(key,value),end = " ")

#print("s_dic1:",s_dic1)
#print("s_dic2:",s_dic2)
'''



'''
for key, value in s_dic1.items() : 
    print("\"{0}\":{1}".format(key,value),end =" ")
else:
    print()
'''
'''
s= dict((k,v) for k in students)
print(s.items())
'''
'''
def sum(k,e,m):
    total = k+e+m
    return total

def aver():
    average = sum(k,e,m) / 3 
    return average
'''

'''
students['total'] = students["kor"]+students["kor"]+students["kor"] 
students['average'] = students['total'] / 3

print(students.item())
'''