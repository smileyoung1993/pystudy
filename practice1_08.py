
##q8

## dict 사용

'''
key ==> menu 
value ==> price

'''
keys = ("오뎅","순대","만두")
values = (300,400,500)
d= dict(zip(keys , values))

menu = input()

for key in d.keys():
    if key == menu:
        print("메뉴:",key,"가격:",d[key])
    
if d[key] != menu:
    print("없는 메뉴입니다.")
    
'''
print(d,type(d))
'''

