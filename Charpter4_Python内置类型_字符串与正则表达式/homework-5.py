"""
--------------------------------------------------------------------------------
接口      : Port-channel1.189
IP地址    : 192.168.189.254
状态      : up
"""

import re

str1 = 'Port-channel1.189   192.168.189.254 YES CONFIG  up  up '

#po = re.match('\D+\d+((/\d+)+(\.\d+)?)?', str1)
po = re.match('\D+[-]?\d+[.]?\d+',str1)
ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str1)

print(ip)
