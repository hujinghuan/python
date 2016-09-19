# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import numexpr as nep#可以执行query语句，并且运算速度快

df = pd.read_excel("sample-salesv3.xlsx")

print(df.dtypes)
df['date'] = pd.to_datetime(df['date'])#改变date的数据格式，从object到datetime
print(df.head())
print(df.dtypes)
print(df[df["account number"]==307599].head())#筛选account number=307599的记录
print(df[df["quantity"]>22].head())
print(df[df["sku"].map(lambda x: x.startswith('B1'))].head())#筛选sku中以B1开头的记录，lambda=λ
print(df[df["sku"].map(lambda x: x.startswith('B1')) & (df["quantity"]>22)].head())#；两个条件用&链接即可
print(df[df["account number"].isin([714466,218895])].head())

df.query('name == ["Kulas Inc","Barton LLC"]')
print(df.query)

df = df.sort_values(by='date')#现在要用sort_values(by=)命令
print(df.head())
print(df[df['date'] >='20140905'].head())
print(df[df['date'] >='2014-03'].head())#直接对月份进行操作也可以
print(df[df['date'] >= 'Oct-2014'].head()) #这么写也可以。。。
print(df[(df['date'] >='20140701') & (df['date'] <= '20140715')].head()) #选择时间间隔

df2 = df.set_index(['date'])#将date设置为index
print(df2.head())
print(df2["20140101":"20140201"].tail())#直接对索引操作
print(df2["2014-Jan-1":"2014-Feb-1"].tail())#这么写当然也可以

print(df[df['sku'].str.contains('B1')].head())#效果与14行命令基本一样，不过范围更广

print(df[(df['sku'].str.contains('B1-531')) & (df['quantity']>40)].sort_values(by=['quantity','name'],ascending=[0,1]))#没有descending命令，[0]表示降序，[1]表示升序

df["name"].unique()
"""
array=([u'Barton LLC', u'Trantow-Barrows', u'Kulas Inc',
       u'Kassulke, Ondricka and Metz', u'Jerde-Hilpert', u'Koepp Ltd',
       u'Fritsch, Russel and Anderson', u'Kiehn-Spinka', u'Keeling LLC',
       u'Frami, Hills and Schmidt', u'Stokes LLC', u'Kuhn-Gusikowski',
       u'Herman LLC', u'White-Trantow', u'Sanford and Sons',
       u'Pollich LLC', u'Will LLC', u'Cronin, Oberbrunner and Spencer',
       u'Halvorson, Crona and Champlin', u'Purdy-Kunde'], dtype=object)
"""
print(df.drop_duplicates(subset=["account number","name"]).head())
print(df.drop_duplicates(subset=["account number","name"]).ix[:,[0,1]])#选取第0~1列