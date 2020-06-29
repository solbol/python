user_strs = ''

while True:
    user_str = input('Введите строку (для выхода введите *): ')
    if user_str != '*':
        user_strs += user_str + '\n'
    else:
        break

with open('user_file.txt', 'w') as f:
    f.write(user_strs)