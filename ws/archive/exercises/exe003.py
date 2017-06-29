# function that converts Celsius degrees to Fahrenheit
def celToFahr(cel):
    if cel < -273.15:
        return ('Too low value')
    else:
        fahr = cel * 1.8 + 32
        return (round(fahr, 4))


print(celToFahr(36.6))
