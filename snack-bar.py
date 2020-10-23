def clear():
    print('\n'*40)


def login():
    users = ['admin']
    passwords = ['admin']

    print('\tHELLO OPERATOR! INSERT YOUR CREDENTIALS:\n')
    # user: admin
    user = input('\tUSER:          ')
    # senha: admin
    password = input('\tPASSWORD:      ')

    if user in users:
        if password == passwords[passwords.index(user)]:
            menu()
        else:
            clear()
            print('\n\tTRY AGAIN!')
            login()
    else:
        clear()
        print('\n\tTRY AGAIN!')
        login()


def menu():
    print('\tCHOOSE AN OPTION:')



login()
