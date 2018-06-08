# dict 

#method 1
d = dict()
print(d,type (d))
# method2 

d = {}
print(d, type(d))

# method 3

d = dict(one = 1 , two = 2 )
print(d,type(d))

# method 4
keys = ("one","two","three")

values = (1,2,3)
print(d,type(d))

d= dict(zip(keys , values))
print(d)

# 사전의 키
print("----------------key")
# 
d= {}
d[10] = "10"
d["baseball"]= 9
d[("kim",10)] = "student"

print(d,type(d))

#d(["lee",30]) = "wokers" type error

# dict method

print("-----------------method")

d= {"baseball":9,"soccer":11, "basketball":5} 
print(d,type(d))

# keys()
print(d.keys())

# values()
print(d.values())

#items()
print(d.items())

# bring values
print(d['baseball'])
print(d['handball'])# keyerror

# bring values 2 : get()
print(d.get('handball'))
print(d.get('handball',"?"))# bagic value??

# delete value
del d['soccer']
print(d)

# clear() 
# d.clear()
print(d)

d = {"baseball":9,"soccer":11,"basketball": 5}
# back
print("------------ back")
d['soccer']=11

# method1 : 
# for key in d:
for key in d.keys():
    print(str(key,":",d[key]))
    
# method2 : 키와 값을 함께 받아와서 활용 : items()
for key, value in d.items() : 
    print("{0}:{1}".format(key,value),end =" ")
else:
    print()
    