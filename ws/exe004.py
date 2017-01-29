temperatures=[10,-20,-289,100]

def celToFahr(cel):
    if cel<-273.15:
        return('Too low value')
    else:
        fahr=cel*1.8+32
        return(round(fahr,4))

for i in temperatures:
    print(celToFahr(i))
