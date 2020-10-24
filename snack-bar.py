def clear():
    print('\n' * 400)


def login():
    users = ['admin']
    passwords = ['admin']

    print('\tHELLO OPERATOR! INSERT YOUR CREDENTIALS:\n')
    # user: admin
    user = input('\tUSER:          ')
    # password: admin
    password = input('\tPASSWORD:      ')

    if user in users:
        if password == passwords[passwords.index(user)]:
            clear()
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
    print('\t1 - NEW BUY                2 - REGISTER PRODUCT')
    print('\t3 - MODIFY A PRODUCT       4 - SALES REPORT')
    print('\t                           0 - LOGOFF')
    option = input('\t')

    if option == '1':
        new_buy()

    elif option == '2':
        register_product()

    elif option == '3':
        modify_product()

    elif option == '4':
        sales_report()

    elif option == '0':
        clear()
        login()

    else:
        print('\tINVALID OPTION, TRY AGAIN:')
        menu()


def new_buy():
    pass


def register_product():
    pass


def modify_product():
    pass


def sales_report():
    pass


# login()
menu()
