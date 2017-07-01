def age_foo(age): # age here is a local variable
    new_age = float(age) + 50
    return new_age

age = input("Enter your age: ")
# age here is a global variable
# print(age_foo(age))

if float(age) < 150:
    print(age_foo(age))
else:
    print("How is that possible?")
