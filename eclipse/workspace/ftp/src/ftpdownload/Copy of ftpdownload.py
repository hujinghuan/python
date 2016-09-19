#!/usr/bin/python  
# -*- coding: utf-8 -*-  

import os
import sys
import ftplib
from  ftplib import FTP
import time,datetime
import sqlite3


DEBUG=False
INFO_DB=os.path.join( os.getcwd(),"0.txt")


class FTPSync(object):
    def __init__(self,INFO_DB=""):

        if not  os.path.isfile( INFO_DB) :
            with open(INFO_DB,"w") as f:
                f.write("0")
                self.is_first_run=True
        else:
            with open(INFO_DB ) as f:
                flag=f.read().strip()
                if   flag=="1":
                    self.is_first_run = True
                else:
                    self.is_first_run = False

        if DEBUG:
            ftp = FTP()
            timeout = 30
            port = 21000
            ftp.connect('192.168.4.66', port, timeout)  # 连接FTP服务器
            ftp.login('user', '123')  # 登录
            print ftp.getwelcome()  # 获得欢迎信息
            # ftp.cwd('test')  # 设置FTP路径
            # print ftp.retrlines('LIST')  # 列出目录内容

            self.conn = ftp
            # self.conn.cwd(r'.\voice')  # 远端FTP目录
            self.conn.cwd('/media/sda/voice')  # 远端FTP目录
            self.conn.set_debuglevel(1)
            os.chdir(r'c:\data')  # 本地下载目录

        else:
            self.conn = ftplib.FTP('192.168.4.66', 'user', '123')
            self.conn.cwd('/media/sda/voice')  # 远端FTP目录
            self.conn.set_debuglevel(1)
            os.chdir('c:\data')  # 本地下载目录


    def get_dirs_files(self,ftp_curr_dir=""):
        u''' 得到当前目录和文件, 放入dir_res列表 '''
        dir_res = []
        self.conn.dir('.', dir_res.append)
        files = [f.split(None, 8)[-1] for f in dir_res if f.startswith('-')]

        dirs = [f.split(None, 8)[-1] for f in dir_res if f.startswith('d')]

        if  not self.is_first_run and  ftp_curr_dir=="/media/sda/voice":
            # 只需要根据检查的日期来进行
            print "ftp_curr_dir",  ftp_curr_dir
            now_dir=datetime.datetime.now().strftime("%Y%m%d")
            if  now_dir in  dirs:
                dirs=[ now_dir ]
            else:
                dirs=[]

        return (files, dirs)

    def walk(self, next_dir):
        print 'Walking to', next_dir
        self.conn.cwd(next_dir)
        try:
            os.mkdir(next_dir)
        except OSError:
            pass
        os.chdir(next_dir)
        ftp_curr_dir = self.conn.pwd()
        local_curr_dir = os.getcwd()
        files, dirs = self.get_dirs_files( ftp_curr_dir)
        print "FILES: ", files
        print "DIRS: ", dirs
        for f in files:
            print next_dir, ':', f
            outf = open(f, 'wb')
            try:
                self.conn.retrbinary('RETR %s' % f, outf.write)
            finally:
                outf.close()
        for d in dirs:
            os.chdir(local_curr_dir)
            self.conn.cwd(ftp_curr_dir)
            self.walk(d)
    def run(self):
        self.walk('.')
def main():
    f = FTPSync( INFO_DB )
    f.run()
if __name__ == '__main__':
    main()
