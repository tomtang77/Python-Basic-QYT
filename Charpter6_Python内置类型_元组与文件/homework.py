#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 打印字典
#
# {('2.168.189.167', '32806', '7.78.5.128', '65247'): ('74', 'UIO'), ('2.168.189.167', '80', '7.78.5.128', '65233'): ('334516', 'UIO')}
#
#
# 格式化打印输出
#
#        src : 2.168.189.167        |     src_p : 32806      |       dst : 7.78.5.128|     dst_p : 65247     |
#      bytes : 74                   |     flags : UIO
# ==============================================================================================================
#        src : 2.168.189.167        |     src_p : 80         |       dst : 7.78.5.128|     dst_p : 65233     |
#      bytes : 334516               |     flags : UIO
# ==============================================================================================================


import re
str1 = """TCP Student  192.168.189.167:32806 Teacher  137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO 
TCP Student  192.168.189.167:80 Teacher  137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO """

str2 = str1.split('\n')
print(str2)

# dict1 = re.match(".*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes\s+(\d+).*flags(\D+)",str2).groups()
# print(dict1)

d1 = {}

for x in str2:
    result = re.search(".*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes\s+(\d+).*flags(\D+)",x).groups()
    key = (result[0], result[1], result[2], result[3])
    value = (result[4], result[5])
    d1[key] = value
print('打印字典\n')
print(d1)

print('\n\n打印格式化輸出\n')

for key, value in d1.items():
    print("="*150)
    print(f'{"src :":>15}{key[0]:<25}' '|' f'{"src_p :":>15}{key[1]:<15}' '|' f'{"dst :":>15}{key[2]:<15}' '|' f'{"dst_p :":>15}{key[3]:<15}')
    print(f'{"bytes :":>15}{value[0]:<25}' '|' f'{"flags :":>15}{value[1]:<15}')
    print("="*150)

