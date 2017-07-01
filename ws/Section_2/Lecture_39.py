def celcius_to_fahrenheit(celcius):
    if float(celcius) < -273.15:
        return "That temperature doesn't make sense!"
    else:
        fahrenheit = float(celcius) * 1.8 + 32
        return fahrenheit

# fahrenheit = celcius_to_fahrenheit(input("Type celcius temperature: "))

# print(fahrenheit)

temperatures=[10,-20,-289,100]

for i in temperatures:
    print(celcius_to_fahrenheit(i))
