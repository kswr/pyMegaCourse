'''
planet=input('What planet are you from? ')
print(planet)
'''
#validates user password
correctPass = 'python123'
password = ''
triesNum = 0
while password != correctPass:
    password=input('Enter password: ')
    triesNum=triesNum+1
    if password == correctPass:
        print('You are logged in!')
    elif triesNum <3:
        print('Sorry, try again')
    else:
        print('Access denied!')
        break
