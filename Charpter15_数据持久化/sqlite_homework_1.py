#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import sqlite3

# Python字典对象，我们将把它写入SQLite数据库
homework_dict = [{'姓名': '学员1', '年龄': 37, '作业数': 1},
                 {'姓名': '学员2', '年龄': 33, '作业数': 5},
                 {'姓名': '学员3', '年龄': 32, '作业数': 10}]

# 连接SQLite数据库
conn = sqlite3.connect('qytanghomework.sqlite')
cursor = conn.cursor()

# 执行创建表的任务
cursor.execute("create table qytang_homework_info (姓名 varchar(40), 年龄 int, 作业数 int)")

# 读取Python字典数据，并逐条写入SQLite数据库
for teacher in homework_dict:
    name = teacher['姓名']
    age = teacher['年龄']
    homework = teacher['作业数']
    cursor.execute("insert into qytang_homework_info values ('%s', %d, %d)" % (name, age, homework))

conn.commit()
