import json


with open('user_file.txt', 'w') as f:
    f.write('firm_1 ООО 10000 5000\n')
    f.write('firm_2 ИП 1000 700\n')
    f.write('firm_3 АО 50000 60000')


my_list = [{}, {}]

with open('user_file.txt') as f:
    profit_sum = 0
    profit_cnt = 0
    for line in f:
        firm_info = line.split()
        profit = int(firm_info[2]) - int(firm_info[3])
        if profit > 0:
            profit_sum += profit
            profit_cnt += 1
        my_list[0].update({firm_info[0]: profit})

    my_list[1].update({'average_profit': profit_sum / profit_cnt})

with open('user_file_new.txt', 'w') as f:
    json.dump(my_list, f)