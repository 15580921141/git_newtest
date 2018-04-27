# coding:utf-8
import sys
import time
import  codecs

import xlrd
def testexcle(keystr):
    data = xlrd.open_workbook('20170818.xls')
    table = data.sheets()[0]
    nrows = table.nrows

    i=0

    for i in range(1,nrows):
        clickstr=table.cell(i,2).value



        if clickstr==keystr:

            break

    # print i
    return table.cell(i,3).value


class Tail():
    def __init__(self,file_name,callback=sys.stdout.write):
        self.file_name = file_name
        self.callback = callback
    def follow(self,n=10):

        with open(self.file_name,"wb") as f:
            f.truncate()

        try:
            with codecs.open(self.file_name,"r","utf-16") as f:

                #先清空文件内容

                self._file = f
                self._file.seek(0,2)
                self.file_length = self._file.tell()
                self.showLastLine(n)



                while True:

                    line = self._file.readline()
                    # print line
                    if line:


                        # self.callback(line)
                        if str(line).startswith("Request url"):
                            line=str(line).replace("%3D","")
                            # self.callback(str(line))



                            print "-----------------------------------------"
                            result=decode_base64(str(line).split("=")[1])

                            if result:
                                # print result.split("\t")

                                buttonnum=result.split("\t")[8]

                            # print buttonnum



                            # try:
                            #     buttonnum=int(buttonnum)
                            # except:
                            #     buttonnum=0

                            # if len (buttonnum)>4 or buttonnum=='null':
                            #     buttonnum=0
                            # else:
                            #     buttonnum=int(buttonnum)
                            #
                                print  u"按钮名称为：\t\t\t"+testexcle(buttonnum)

                                print u"按钮数值为\t\t\t\t"+str(buttonnum)
                            else:
                                print str(line).split("=")[1]





                            # print str(line)
                            # print decode_base64(str(line).split("=")[-1])
                            # self.callback(decode_base64(str(line).split("=")[-1]))
                            # print ("\n")
                            # self.callback(u"按钮为"+decode_base64(str(line).split("=")[-1]).split("\t")[8])
                            # print decode_base64(str(line).split("=")[-1]).split("\t")[8]
                    # time.sleep(1)

        except Exception,e:
            print u'打开文件失败，囧，看看文件是不是不存在，或者权限有问题'
            print e


    def showLastLine(self, n):
        len_line = 100
        read_len = len_line*n
        last_lines=""

        while True:
            if read_len>self.file_length:
                self._file.seek(0)
                last_lines = self._file.read().split('\n')[-n:]
                break
            self._file.seek(-read_len, 2)
            last_words = self._file.read(read_len)
            count = last_words.count('\n')
            if count>=n:
                last_lines = last_words.split('\n')[-n:]
                break
            else:
                if count==0:
                    len_perline = read_len
                else:
                    len_perline = read_len/count
                read_len = len_perline * n
        # for line in last_lines:
        #
        #     self.callback(line+'\n')

import base64

def decode_base64(data):

    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    try:

        return base64.b64decode(data)
    except:
        pass








if __name__ == '__main__':


    py_tail = Tail('D:\\Fiddler Sessions\Api\\apptj.tianqikb.com\\123.txt')
    py_tail.follow()

