temperatures=[10,-20,-289,100]

def writer(temps):
    with open('exe005out.txt','w') as file:
        for c in temps:
            if c >= -273.15:
                f=c*1.8+32
                file.write(str(f)+'\n')

writer(temperatures)
