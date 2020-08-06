#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
--------------------------------------------------------------------------------
接口      : Port-channel1.189
IP地址    : 192.168.189.254
状态      : up
"""

import re
a = '接口'
b = 'IP地址'
c = 'status'
str1 = 'Port-channel1.189   192.168.189.254 YES CONFIG  up  up '

#po = re.match('\D+\d+((/\d+)+(\.\d+)?)?', str1)
po = re.match(r'(\D+[-]?\d+[.]?\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*)\s*',str1).groups()
#ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str1)
#status = re.search(('up'), str1)
print(po)
print('-'*80)
print(f'{a:<7}: {po[0]:<10}')
print(f'{b:<7}: {po[1]:<10}')
print(f'{c:<8}: {po[-1]:<10}')


