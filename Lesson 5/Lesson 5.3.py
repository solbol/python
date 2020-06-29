with open('user_file.txt', 'w') as f:
    f.write('Смирнов оклад 20000\n')
    f.write('Васильев оклад 30000\n')
    f.write('Иванов оклад 15000\n')
    f.write('Петров оклад 18000\n')
    f.write('Сидоров оклад 25000')


with open('user_file.txt') as f:
    salary_sum = 0
    salary_cnt = 0
    for line in f:
        user_info = line.split()
        if int(user_info[2]) <= 20000:
            print(f'Сотрудник {user_info[0]} имеет оклад меньше 20 тыс. руб.')
        salary_sum += int(user_info[2])
        salary_cnt += 1

print(f'Средняя зарплата {salary_sum / salary_cnt} руб.')