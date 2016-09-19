#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
import os
import time   
import sys
import ftplib

sourceDir = ftplib.FTP('192.168.4.66', 'user', '123')
sourceDir.cwd('/media/sda/log')
targetDir = (r"D:\data")  
copyFileCounts = 0
  
def copyFiles(sourceDir, targetDir):   
    global copyFileCounts
    #print (sourceDir)
    #print (u"%s current folder%has delt with%s files" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), sourceDir,copyFileCounts))
    for f in os.listdir(sourceDir.cwd):
        sourceF = os.path.join(sourceDir, f)
        targetF = os.path.join(targetDir, f)
                 
        if os.path.isfile(sourceF):   
            #创建目录   
            if not os.path.exists(targetDir): 
                os.makedirs(targetDir)
            copyFileCounts += 1
               
            #文件不存在，或者存在但是大小不同，覆盖   
            if not os.path.exists(targetF) or (os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                #2进制文件   
                open(targetF, "wb").write(open(sourceF, "rb").read())
                #print (u"%s %s copy finished" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF))
            else:  
                #print (u"%s %s already exist,can't copy" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF))
                print('')
           
        if os.path.isdir(sourceF):   
            copyFiles(sourceF, targetF)   
          
if __name__ == "__main__":
    try:   
        import psyco
        psyco.profile()   
    except ImportError:
        pass
    copyFiles(sourceDir,targetDir)