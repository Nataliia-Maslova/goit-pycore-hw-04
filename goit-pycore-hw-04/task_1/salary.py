import re
from pathlib import Path


def total_salary(path):
    with open(path, "r") as salary_txt:
        string = salary_txt.read()
        pattern = r'\d+'
        salary_list = re.findall(pattern, string)
        salary_nums = [eval(i) for i in salary_list]
        total_salary = sum(salary_nums)
        workers_number = len(salary_nums)
        avarage_salary = int(total_salary / workers_number)
        res = (total_salary, avarage_salary)
        print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {avarage_salary}.")
        return(res)

path_salary = Path("task_1/salary.txt")
if path_salary.is_file():
    total_salary(path_salary)