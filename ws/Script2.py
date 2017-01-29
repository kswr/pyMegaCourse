def currency_converter(rate, euros):
    dollars=euros*rate
    return dollars

rate=input('Whats the euro rate? ')
euros=input('How much money do you have? ')
print('You have '+str(currency_converter(float(rate), float(euros)))+' USD')

#creates list functions
'''
functions=[currency_converter(100,1000),currency_converter(100,2000)]
print(functions)
'''
