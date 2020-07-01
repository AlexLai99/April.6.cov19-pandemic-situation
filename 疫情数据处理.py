# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:43:13 2020

@author: laijianqiang
"""
import requests
import pandas as pd
import time

#data = requests.get('https://lab.isaaclin.cn/nCoV/api/area?latest=0')
#data = data.json()
#res = data['results']
#df = pd.DataFrame(res)
df=pd.read_csv('D:/Onedrive/疫情/DXYArea0407.csv')
def time_c(timeNum):
    timeTemp = float(timeNum/1000)
    tupTime = time.localtime(timeTemp)
    standardTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    return standardTime

#for i in range(len(df)):
    #df.iloc[i,11] = time_c(df.iloc[i,11])

for i in range(len(df)):
    df.iloc[i,11] = df.iloc[i,11][5:10]

#df.to_excel('D:/Onedrive/疫情/疫情实时数据0313.xlsx')
df.replace('Burma','Myanmar',inplace=True)
df.loc[df['countryName']=='吉尔吉斯斯坦', 'countryEnglishName'] = 'Kyrgyzstan'
df[df['countryName']=='吉尔吉斯斯坦']['countryEnglishName']
df.loc[df['countryName']=='南苏丹', 'countryEnglishName'] = 'S. Sudan'
df.loc[df['countryName']=='格陵兰', 'countryEnglishName'] = 'Greenland'
df.loc[df['countryName']=='刚果（金）', 'countryEnglishName'] = 'Dem. Rep. Congo'
df.loc[df['countryName']=='刚果（布）', 'countryEnglishName'] = 'Congo'
df.loc[df['countryName']=='赞比亚共和国', 'countryEnglishName'] = 'Zambia'
df.loc[df['countryName']=='科特迪瓦', 'countryEnglishName'] = "Côte d'Ivoire"
df.loc[df['countryName']=='东帝汶', 'countryEnglishName'] = "Timor-Leste"
df.loc[df['countryName']=='黑山', 'countryEnglishName'] = "Montenegro"
df.loc[df['countryName']=='塞尔维亚', 'countryEnglishName'] = "Serbia"
df.loc[df['countryName']=='北马其顿', 'countryEnglishName'] = "Macedonia"
df.loc[df['countryName']=='黑山', 'countryEnglishName'] = "Montenegro"
df.loc[df['countryName']=='柬埔寨', 'countryEnglishName'] = "Cambodia"
df.loc[df['countryName']=='不丹', 'countryEnglishName'] = "Bhutan"
df.loc[df['countryName']=='黑山', 'countryEnglishName'] = "Montenegro"
df.loc[df['countryName']=='塔吉克斯坦', 'countryEnglishName'] = "Tajikistan"
df.loc[df['countryName']=='土库曼斯坦', 'countryEnglishName'] = "Turkmenistan"
df.loc[df['countryName']=='索马里', 'countryEnglishName'] = "Somalia"
df.loc[df['countryName']=='也门', 'countryEnglishName'] = "Yemen"
df.loc[df['countryName']=='美国', 'countryEnglishName'] = "United States"
df.loc[df['countryName']=='英国', 'countryEnglishName'] = "United Kingdom"
df.loc[df['countryName']=='波黑', 'countryEnglishName'] = "Bosnia and Herz."
df.loc[df['countryName']=='捷克', 'countryEnglishName'] = "Czech Rep."
df.loc[df['countryName']=='莱索托', 'countryEnglishName'] = "Lesotho"
df.loc[df['countryName']=='毛里塔尼亚', 'countryEnglishName'] = "Mauritania"
df.loc[df['countryName']=='斯里兰卡', 'countryEnglishName'] = "Sri Lanka"
df.loc[df['countryName']=='布隆迪共和国', 'countryEnglishName'] = "Burundi"
df.loc[df['countryName']=='卢旺达', 'countryEnglishName'] = "Rwanda"
df.loc[df['countryName']=='多米尼加', 'countryEnglishName'] = "Dominican Rep."
df.loc[df['countryName']=='厄立特里亚', 'countryEnglishName'] = "Eritrea"
df.loc[df['countryName']=='中非共和国', 'countryEnglishName'] = "Central African Rep."
df.loc[df['countryName']=='老挝', 'countryEnglishName'] = "Lao PDR"
df.loc[df['countryName']=='厄立特里亚', 'countryEnglishName'] = "Eritrea"
df.loc[df['countryName']=='新喀里多尼亚', 'countryEnglishName'] = "New Caledonia"
df.loc[df['countryName']=='福克兰群岛', 'countryEnglishName'] = "Falkland Is."
df.loc[df['countryName']=='几内亚比绍', 'countryEnglishName'] = "Guinea-Bissau"
df.loc[df['countryName']=='赤道几内亚', 'countryEnglishName'] = "Eq.Guinea"
df.loc[df['countryName']=='佛得角', 'countryEnglishName'] = "Cape Verde"

date=pd.read_excel('D:/Onedrive/疫情/date.xlsx')['日期']
tem = df[df['updateTime'] == '01-22']
tem = tem.drop_duplicates(['provinceName'], keep='first')
#截止到04-07
for i in date[3:79]:
    tem1 = df[df['updateTime'] == i]
    tem1 = tem1.drop_duplicates(['provinceName'], keep='first')
    tem = tem.append(tem1)

tem = tem.reset_index(drop=True)
tem.to_excel('D:/Onedrive/疫情/去重0407.xlsx')

country=df.drop_duplicates(['countryName'],keep='first')['countryEnglishName']
country = country.reset_index(drop=True)

#截止到04-07
date = date[2:79].reset_index(drop=True)
df3=[]
for i in country:
    df1=[]
    for j in date:
        province=tem[tem['countryEnglishName'] == i][tem['updateTime'] == j]['provinceName'].reset_index(drop=True)
        a=tem[tem['countryEnglishName'] == i][tem['updateTime'] == j].sum()['province_confirmedCount']
        for k in province:
            #特殊情况：中国总计和各省总计容易混淆
            if k==i:
                a=tem[tem['countryName'] == k][tem['updateTime'] == j][tem['provinceName'] == k]['province_confirmedCount'].reset_index(drop=True)[0]
            else:
                pass
        df1.append(a)
    df3=pd.concat([pd.DataFrame(df3),pd.DataFrame(df1)],axis=1)
df3.columns = country.tolist()
df3=pd.concat([date,df3],axis=1)
df3.to_excel('D:/Onedrive/疫情/确诊人数时间序列0407.xlsx')
print ('已完成确诊数据清洗')

tem.drop_duplicates(['provinceName','updateTime'],keep='first',inplace=True)
tem=tem.reset_index(drop=True)
df4=[]
for i in country:
    d1=[]
    d2=[]
    d3=[]
    for j in date:
        province=tem[tem['countryEnglishName'] == i][tem['updateTime'] == j]['provinceEnglishName'].reset_index(drop=True)
        a=tem[tem['countryEnglishName'] == i][tem['updateTime'] == j].sum()['province_confirmedCount']
        for k in province:
            #特殊情况：中国总计和各省总计容易混淆
            if k==i:
                b=tem[tem['countryEnglishName'] == k][tem['updateTime'] == j][tem['provinceEnglishName'] == k]['province_confirmedCount'].reset_index(drop=True)[0]
            else:
                pass
        d1.append(b)
        d3.append(j)
        d2.append(i)
    d2=pd.concat([pd.DataFrame(d2),pd.DataFrame(d1)],axis=1)
    d3=pd.concat([pd.DataFrame(d3),pd.DataFrame(d2)],axis=1)
    df4=pd.concat([pd.DataFrame(d3),pd.DataFrame(df4)],axis=0).reset_index(drop=True)
    
df4.columns=['date','country','confirmedCount']
#df4.dropna(axis=0,how='any')
df4.fillna(0,inplace=True)
df4=df4[~df4['country'].isin([0])]
df4.to_excel('D:/Onedrive/疫情/确诊人数0407可用时间序列数据.xlsx')
df5=df4[df4['country'].isin(['United States','France','Germany','Italy','Japan','China','India','Korea','Spain'])]
df5.to_excel('D:/Onedrive/疫情/重点国家确诊人数0407.xlsx')
print ('已完成可视化确诊数据清洗')