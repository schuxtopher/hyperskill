with open('salary.txt', 'r') as in_file, open('salary_year.txt', 'w') as out_file:
    for salary in in_file:
        yearly_salary = int(salary) * 12
        line = str(yearly_salary) + '\n'
        out_file.write(line)
