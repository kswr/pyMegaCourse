def celcius_to_fahrenheit(celcius):
    fahrenheit = float(celcius) * 1.8 + 32
    return fahrenheit

fahrenheit = celcius_to_fahrenheit(input("Type celcius temperature: "))

print(fahrenheit)
