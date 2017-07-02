def celcius_to_fahrenheit(celcius):
    if float(celcius) < -273.15:
        return "It's too low"
    else:
        fahrenheit = float(celcius) * 1.8 + 32
        return fahrenheit

fahrenheit = celcius_to_fahrenheit(input("Type celcius temperature: "))

print(fahrenheit)
