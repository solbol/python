with open('user_file.txt', 'w') as f:
    f.write('One — 1\n')
    f.write('Two — 2\n')
    f.write('Three — 3\n')
    f.write('Four — 4')


new_file = ''

with open('user_file.txt') as f:
    my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for line in f:
        for key, val in my_dict.items():
            line = line.replace(key, val)
        new_file += line


with open('user_file_new.txt', 'w') as f:
    f.write(new_file)