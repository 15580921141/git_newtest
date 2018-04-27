#coding:utf-8
import os
import time

#文件名为时间，目录名为日期
source = ['E:\\lixin\\home','E:\\lixin\\home\\swaroop']

target_dir ='D:\\LX\\backups\\'

target = time.strftime('%H%M%S')#文件名

now=target_dir+time.strftime('%Y%m%d')#目录名

if not os.path.exists(now):
    os.mkdir(now)
    print('Successful make',now)
today=now+os.sep+target+'.zip'
zip_command ="rar a %s %s"% (today, ' '.join(source))

if os.system (zip_command) == 0:
    print 'Successful backup to', today
else:
    print 'Backup FAILED '