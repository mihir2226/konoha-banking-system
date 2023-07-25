import math
from random import randint

user ={}
customers = {
    7383031433:{
    'name':'mihir',
    'age':22,
    'gender':'male',
    'aadhar':533050075033,
    'acc_num':7383031433,
    'acc_pass':'mihirnayak',
    'balance':3000}
}

def signup(user,customers):
    name = input('\nEnter your name : ')

    flag=0
    while True:
        if flag==0:
            try:
                age = int(input('Enter your age : '))
                if len(str(age)) > 3 or str(age).isnumeric() == False:
                    raise ValueError('Enter valid age...')
                flag=1
            except ValueError as e:
                print(str(e))

        if flag==1:
            try:
                gender = int(input('gender\n(1) Male\n(2) Female\n->>'))

                if gender==1:
                    gender = 'male'
                    flag=2
                elif gender==2:
                    gender='female'
                    flag=2
                elif gender>2 and gender==0:
                    raise ValueError('Choose valide option...')
            except ValueError as e:
                print(str(e))

        if flag==2:
            try:
                aadhar = int(input('Enter your aadhar number : '))
                if len(str(aadhar))<11 and len(str(aadhar)) != 12:
                    raise ValueError('enter valid Aadhar number!!')
                break
            except ValueError as e:
                print(str(e))

    acc_pass = input('Create your password : ')

    user['name'] = name
    user['age'] = age
    user['gender'] = gender
    user['aadhar'] = int(aadhar)
    user['acc_pass'] = acc_pass

    flag=3
    while True:
        if flag==3:
            try:
                balance = int(input('\nDeposite money in your account : '))
                user['balance'] = balance

                if balance < 2000:
                    raise ValueError('\nDeposite minimum 2000 to your account!!')
                else:
                    account_num = randint(1000000000, 9999999999)
                    user['acc_num'] = account_num
                    if user['acc_num'] not in customers:
                        print('Your Account is Generating...')
                        # account_num = randint(1000000000, 9999999999)
                        print(f"\nCongratulation {user['name']} your account created successfully..\nYour account number is {user['acc_num']}")
                        customers[account_num] = user
                        # print(customers)
                        start(customers)
            except ValueError as e:
                print(str(e))
def start(customers):
    while True:
        try:
            print('\n---------------------------------------------------')
            print('Welcome to Konoha bank!!')
            choice = int(input('what do you like to do?\n(1) Existing User\n(2) New User\n(3) Exit\n->>'))

            if choice == 1:
                login(customers)
            if choice == 2:
                signup(user,customers)
            if choice == 3:
                print('Thank you for visiting our bank!!')
                print('---------------------------------------------------')
                break
            if choice not in [1,2,3]:
                raise ValueError('Invalid input!!')
        except ValueError as e:
            print(str(e))

def login(customers):
    # lacc = 738303143326
    # lpass = 'mihirnayak'
    flag = 0
    while True:
        if flag == 0:
            try:
                lacc = int(input('\nEnter your account number : '))
                if lacc in customers:
                    flag=1
                else:
                    raise ValueError('Enter valid Account Number...\n')

            except ValueError as e:
                print(str(e))

        if flag==1:
            try:
                lpass = input('Enter your password : ')
                if lpass == customers[lacc]['acc_pass']:
                    print('Login successfully...')
                    bank(lacc,customers)
                else:
                    raise ValueError('Password does not match..')

            except ValueError as e:
                print(str(e))

def bank(lacc,customers):
    if customers[lacc]['gender'] == 'male':
        print(f"\nWelcome Mr.{customers[lacc]['name']}...")
    else:
        print(f"\nWelcome  Miss.{customers[lacc]['name']}...")

    choice = int(input('what do you want to do?\n(1) Deposite\n(2) Withdraw\n(3) Show Balance\n(4)Back to Main Menu\n-->'))

    if choice == 1:
        print(f"\nBalance : {customers[lacc]['balance']}")
        customers[lacc]['balance'] += int(input('enter the Amount you want to deposite : '))
        bank(lacc, customers)

    if choice == 2:
        print(f"\nBalance : {customers[lacc]['balance']}")
        wm = int(input('enter the Amount you want to withdraw : '))

        if customers[lacc]['balance']-wm < 2000:
            print('You dont have suficient balance...')
            bank(lacc, customers)
        else:
            customers[lacc]['balance'] -= wm
            bank(lacc, customers)

    if choice == 3:
        print(f"\nYour Account Balance is {customers[lacc]['balance']}")
        bank(lacc, customers)

    if choice == 4:
        start(customers)

    if choice not in [1,2,3,4]:
        print('Enter valid input!!')
        bank(lacc, customers)

start(customers)