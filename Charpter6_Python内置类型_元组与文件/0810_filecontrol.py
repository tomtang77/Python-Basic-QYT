#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os

# os.mkdir('test')
# os.chdir('test')
# qytang1 = open('qytang1', 'w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
# qytang2 = open('qytang2', 'w')
# qytang2.write('test file\n')
# qytang2.write('qytang python\n')
# qytang2.close()
# qytang3 = open('qytang3', 'w')
# qytang3.write('test file\n')
# qytang3.write('this is python\n')
# qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')
os.chdir('test')

qytang_file_list = []

open_file = os.listdir() #列出當前目錄下的資料
print(open_file)

for file in open_file:
    if os.path.isfile(file): #看資料是文件還是資料夾，如果是文件的話執行下一步方式
        for file_line in open(file):  #開啟文件
            if 'qytang' in file_line:  #看qytang是否在文件中，如果ＴＲＵＥ執行下一步
                qytang_file_list.append(file) #將檔名塞進qytang_file_list

print('文件中包含"qytang"關鍵字的文件為：')
for x in qytang_file_list:
    print(x)




