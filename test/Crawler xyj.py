#coding:utf-8
import sys
import codecs
import re
f=open('D:/Pythontest/fullstack-data-engineer-master/data/xyj.txt','rb')
con_txt=f.read().decode('utf-8')
con_txt = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+", "",con_txt)
content=con_txt.encode('utf-8').decode('utf-8-sig')

# print(line)
'---------------------------'
# 不同的汉字个数
su=0
con={}
for line in content :
	if len(line) == 0:
		continue
	for j in range(len(line)) :
		# if not line[j] in con:
		if line[j] in ['','\t','\n','，','。','（','）',':','：','□','？','！','《','》','、','；','“','”','__','/','[',']']:
			continue
		if not line[j] in con:
			con[line[j]]=0
		con[line[j]]+=1
f.close()
def get_key(dic,value) :
	for k,v in dic.items():
		if v==value :
			print('出现最频繁的字有：',k)
# for i in range(10):
# 	print(con[i])
print('共出现',len(con),'个不同汉字')
# print('不同汉字出现列表如下：\n',con)
get_key(con,max(con.values()))
con=sorted(con.items(),key=lambda d:d[1],reverse=True)
fg=open('result.csv','w',encoding='utf-8')
for itme in con :

	fg.write(itme[0]+','+str(itme[1])+'\n')
fg.close()

# a={'Jack': 64,'Peter':98,'Tina':64}
#
# def get_key(dic,value):
# 	for k,v in dic.items():
#
# 		if v == value :
# 			print(k)
# get_key(a,64)
# b=list(a.keys())[list(a.values()).index()]
# print(b)

inputStr="hello python,ni hao c,zai jian python"
replaceStr=re.sub(r"hello (\w+),ni hao (\w+),zai jian \1","PHP",inputStr)
print(replaceStr)