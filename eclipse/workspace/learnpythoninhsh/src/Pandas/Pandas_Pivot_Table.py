# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import numexpr as nep#可以执行query语句，并且运算速度快

df = pd.read_excel('sales-funnel.xlsx')
print(df.head())

df["Status"] = df["Status"].astype("category") #把status的type设置为category
df["Status"].cat.set_categories(["won","pending","presented","declined"],inplace=True)#设置category内容

print(pd.pivot_table(df,index=["Manager","Rep"]))#设置manger,rep为pivot_table的index，直接汇总
#print(pd.pivot_table(df,index=["Manager","Rep"],values=["Price"]))#精简表格，只留下price这列，默认price取的平均值
print(pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],aggfunc=[np.sum,len])) #aggfunc=np.sum，求和函数,len=count，计数
print(pd.pivot_table(df,index=["Manager","Rep"],values=["Price","Quantity"],columns=["Product"],aggfunc=[np.sum],fill_value=0))
print(pd.pivot_table(df,index=["Manager","Rep","Product"],values=["Price","Quantity"],aggfunc=[np.sum],fill_value=0))
print(pd.pivot_table(df,index=["Manager","Rep","Product"],values=["Price","Quantity"],aggfunc=[np.sum,np.mean],fill_value=0,margins=True))
print(pd.pivot_table(df,index=["Manager","Status"],values=["Price"],aggfunc=[np.sum],fill_value=0,margins=True))
print(pd.pivot_table(df,index=["Manager","Status"],columns=["Product"],values=["Quantity","Price"],aggfunc={"Quantity":len,"Price":np.sum},fill_value=0))

table = pd.pivot_table(df,index=["Manager","Status"],columns=["Product"],values=["Quantity","Price"],aggfunc={"Quantity":len,"Price":[np.sum,np.mean]},fill_value=0)
print(table)
#table.to_csv('123.csv')

print(table.query('Manager == ["Debra Henley"]'))
print(table.query('Status == ["pending","won"]'))   