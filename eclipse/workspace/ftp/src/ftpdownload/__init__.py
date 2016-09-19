#!/usr/bin/python
#-*- coding: utf-8 -*-

from ftplib import FTP

def ftpconnect():
    ftp_server = 'ftp3.ncdc.noaa.gov'
    username = ''
    password = ''
    ftp=FTP()
    ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
    ftp.connect(ftp_server,21) #连接
    ftp.login(username,password) #登录，如果匿名登录则用空串代替即可
    return ftp

def downloadfile():  
    ftp = ftpconnect()    
    #print ftp.getwelcome() #显示ftp服务器欢迎信息
    datapath = "/pub/data/noaa/"
    year=1911
    while year<=1930:
        path=datapath+str(year)
        li = ftp.nlst(path)
        for eachFile in li:
            localpaths = eachFile.split("/")
            localpath = localpaths[len(localpaths)-1]
            localpath='weatherdata/'+str(year)+'--'+localpath#把日期放在最前面，方便排序
            bufsize = 1024 #设置缓冲块大小      
            fp = open(localpath,'wb') #以写模式在本地打开文件
            ftp.retrbinary('RETR ' + eachFile,fp.write,bufsize) #接收服务器上文件并写入本地文件
        year=year+1
    ftp.set_debuglevel(0) #关闭调试
    fp.close()
    ftp.quit() #退出ftp服务器


if __name__=="__main__":
    downloadfile()
