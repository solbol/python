with open('user_file.txt', 'w') as f:
    f.write('Информатика: 100(л) 50(пр) 20(лаб)\n')
    f.write('Физика: 30(л) — 10(лаб)\n')
    f.write('Физкультура: — 30(пр) —')


with open('user_file.txt') as f:
    my_dict = {}
    for line in f:
        subject = line[:line.find(':')]
        hours_total = 0
        line = line.replace('(', ' ')
        for i in line.split():
            if i.isdigit():
                hours_total += int(i)
        my_dict.update({subject: hours_total})

    print(my_dict)