def celcius_to_fahrenheit(celcius):
    if float(celcius) > -273.15:
        fahrenheit = float(celcius) * 1.8 + 32
        return fahrenheit


temperatures=[10,-20,-289,100]

for i in temperatures:
    print(celcius_to_fahrenheit(i))

with open("..\\output\\Lecture_47_output.txt",'w') as file:
    for i in temperatures:
        file.write((str(celcius_to_fahrenheit(i))+"\n"))
