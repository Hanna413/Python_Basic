def user_data(first_name, last_name, birth_year, curr_place, email, phone):
    user_list = [first_name, last_name, birth_year, curr_place, email, phone]
    print(' '.join(user_list))


user_data(first_name=input('Enter your first name: '), last_name=input('Enter your last name: '),
          birth_year=input('Enter the year of birth: '), curr_place=input('Enter your city/town: '),
          email=input('Enter your e-mail: '), phone=input('Enter your phone: '))
