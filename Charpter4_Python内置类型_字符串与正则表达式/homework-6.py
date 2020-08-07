#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
--------------------------------------------------------------------------------
VLAN ID    : 166
MAC        : 54a2.74f7.0326
Type       : DYNAMIC
Interface  : Gi1/0/11
"""
import re

str1 = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'

#result = re.match(r'(\d\d\d)\s+(\w+\.\w+\.\w+)\s+(\S+)\s+(\w+/\s/\s+)',str1).groups()
result = re.match(r'(\d\d\d)\s+(\w+\.\w+\.\w+)\s+(\S+)\s+(\w+.\d.\d+)', str1).groups()

print(result)

print('='*80)
print(f'{"VLAN ID":<10}: {result[0]:<15}')
print(f'{"MAC":<10}: {result[1]:<15}')
print(f'{"Type":<10}: {result[2]:<15}')
print(f'{"Interface":<10}: {result[3]:<15}')





