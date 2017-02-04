import datetime

filename=datetime.datetime.now()

def createFile():
    '''this script creates an empty file'''
    with open(filename.strftime('%Y-%m-%d-%H-%M'),'w') as file:
        file.write('')

createFile()
