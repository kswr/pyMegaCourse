import math

#function that converts Celsius degrees to Fahrenheit
def celToFahr(cel):
    fahr=cel*1.8+32
    return(round(fahr,4))

print(celToFahr(36.6))
