#quiz01_4
'''
+------------+-----+-----------+
| date       | dow | price     |
+------------+-----+-----------+
| 2018.01.05 | 금  | 2,497.52  |
| 2018.01.04 | 목  | 2,466.46  |
| 2018.01.03 | 수  | 2,486.35  |
| 2018.01.02 | 화  | 2,479.65  |
+------------+-----+-----------+
'''

lst_date = ['2018.01.05','2018.01.04','2018.01.03','2018.01.02']
lst_dow = ['화','수','목','금']
lst_price = [2479.65, 2486.35, 2466.46, 2497.52]

kospi_price = {}

#kospi_price[lst_date[0]] = {"dow": lst_dow[0], "price": lst_price[0]} 
for i in range(len(lst_date)):
    kospi_price[lst_date[i]]={"dow": lst_dow[i], "price": lst_price[i]}

#print(kospi_price)

for i in range(1, len(lst_date)): # 0번인덱스를 안포함 2018년 01월 02일 뺌
    kospi_price[lst_date[i]]['price_diff'] = lst_price[i] - lst_price[i-1] # 전날가격뺌

#print(kospi_price)
print("price_diff: %f" %kospi_price["2018.01.05"]['price_diff'])
print("max:{},min:{}".format(max(lst_price),min(lst_price)))

