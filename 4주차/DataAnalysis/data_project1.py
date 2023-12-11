import pandas as pd
import numpy as np
data = pd.read_csv("C:/Users/user/OneDrive/바탕 화면/데브코스-데이터분석2/4주차/data_sales (1).csv")
print(data.columns)

data['Retailer'].fillna("ETC",inplace=True)
for i,d in enumerate(data['Retailer']):
    # print(type(d))
    if d == 'Kohl\'s':
        data.loc[i,'Retailer'] = 'Kohls'
    else:
        new_d = d.replace(" ", "").lower()


data['Retailer ID'].fillna(0,inplace=True)
id_list = [1128299,1185732,1189833,1197831]
for i,d in enumerate(data['Retailer ID']):
    if d not in id_list:
        id_list.append(d)
    new_d = id_list.index(d)
    data.loc[i, 'Retailer ID'] = new_d

data['Invoice Date'].fillna("0001-01-01",inplace=True)
for i,d in enumerate(data['Invoice Date']):
    # print(type(d))
    a = d.split('/')
    temp = a[2]
    temp2 = a[1]
    a[1] = a[0]
    a[2] = temp2
    a[0] = temp
    new_d = '-'.join(a)
    data.loc[i,'Invoice Date'] = new_d

data['Region'].fillna("ETC",inplace=True)
# for i,d in enumerate(data['Region']):
#     print(type(d))

data['State'].fillna("ETC",inplace=True)
for i,d in enumerate(data['State']):
    # print(type(d))
    new_d = d.replace(" ","")
    data.loc[i,'State'] = new_d


data['City'].fillna("ETC",inplace=True)
for i,d in enumerate(data['City']):
    # print(type(d))
    new_d = d.replace(" ","")
    data.loc[i,'City'] = new_d

data['Product'].fillna("ETC",inplace=True)
for i,d in enumerate(data['Product']):
#   print(type(d))
    temp_d = d.lower()
    if temp_d.find("women"):
        if temp_d.find("footwear"):
            if temp_d.find("athletic"):
                new_d = "waf"
            else:
                new_d = "wsf"
        else:
            new_d = "wa"
    else:
        if temp_d.find("footwear"):
            if temp_d.find("athletic"):
                new_d = "maf"
            else:
                new_d = "msf"
        else:
            new_d = "ma"
    data.loc[i,'Product'] = new_d


data['Price per Unit'].fillna(0,inplace=True)
for i,d in enumerate(data['Price per Unit']):
    if d == 0:
        new_d = 0
    else:
        new_d = int(d[1:-4])
    data.loc[i,'Price per Unit'] = new_d

data['Units Sold'].fillna(0,inplace=True)
for i,d in enumerate(data['Units Sold']):
    # print(type(d))
    new_d = int(d.replace(',',""))
    data.loc[i,'Units Sold'] = new_d

data['Total Sales'].fillna(0,inplace=True)
for i,d in enumerate(data['Total Sales']):
    # print(type(d))
    new_d = d
    if not d.isdigit():
        new_d = int(d.replace(',',""))
    data.loc[i,'Total Sales'] = new_d

data['Operating Profit'].fillna(0,inplace=True)
for i,d in enumerate(data['Operating Profit']):
    new_d = int(d.replace(',',"").replace("$",""))
    data.loc[i,'Operating Profit'] = new_d

data['Sales Method'].fillna("ETC",inplace=True)
for i,d in enumerate(data['Sales Method']):
#   print(type(d))
    temp_d = d.lower()
    if temp_d.find("on"):
        if temp_d.find("line"):
            new_d = "on"
        else:
            new_d = 'out'
    else:
        new_d = "in"
    data.loc[i,'Sales Method'] = new_d


with pd.option_context('display.max_columns',None):
    print(data.head(10))

## 1차 전처리 완료
## 일단 Retailer, Region 다 약어로 고쳐보자
## State, City는 소문자로 그냥 통일