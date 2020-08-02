department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456

#line1 = 'Department1 Name: %-12s Manager: %-12s Course Fees: %-10.2f The End!' % (department1,depart1_m,COURSE_FEES_SEC)
#line2 = 'Department2 Name: %-12s Manager: %-12s Course Fees: %-10.2f The End!' % (department2,depart2_m,COURSE_FEES_Python)
#line1 = 'Department1 Name: {0:<10} Manager:{1:<10} Course Fees:{2:<10.2f} The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
#line2 = 'Department2 Name: {0:<10} Manager:{1:<10} Course Fees:{2:<10.2f} The End!'.format(department2,depart2_m,COURSE_FEES_Python)
line1 = f"Department1 Name: {department1:<10} Manager:{depart1_m:<10} Course Fees:{COURSE_FEES_SEC:<10.2f} The End!"
line2 = f"Department1 Name: {department2:<10} Manager:{depart2_m:<10} Course Fees:{COURSE_FEES_Python:<10.2f} The End!"

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)

