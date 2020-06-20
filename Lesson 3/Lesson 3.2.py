def print_user_data(**kwargs):
    name = kwargs.get('name')
    surname = kwargs.get('surname')
    birth = kwargs.get('birth')
    city = kwargs.get('city')
    email = kwargs.get('email')
    phone = kwargs.get('phone')
    print(f'Имя: {name}, фамилия: {surname}, год рождения: {birth}, город рождения: {city}, e-mail: {email}, телефон: {phone}')

print_user_data(name = 'Иван', surname = 'Петров', birth = 2010, city = 'Москва', email = 'asd@asd.com,', phone = '+7 (123) 456-78-90')