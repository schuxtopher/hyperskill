# put your python code here
students_class1 = int(input())
students_class2 = int(input())
students_class3 = int(input())

tables_class1 = students_class1 // 2 + students_class1 % 2
tables_class2 = students_class2 // 2 + students_class2 % 2
tables_class3 = students_class3 // 2 + students_class3 % 2

sum_tables = tables_class1 + tables_class2 + tables_class3

print(sum_tables)
