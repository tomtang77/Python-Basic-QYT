#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import os

os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1', 'w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2', 'w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3', 'w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')

qytang_file_list = []

file_list = os.listdir()

for file in file_list:
    if os.path.isfile(file):
        for file_line in open(file):
            if 'qytang' in file_line:
                qytang_file_list.append(file)

print('文件中包含"qytang"关键字的文件为:')
for file in qytang_file_list:
    print('\t', end='')
    print(file)
print('\n')
