# Python Mega course

## Section 1 - Getting Started

### Lecture 1 - Introduction

Course author - __Ardit Sulce__, Python and GIS Expert, Founder of PythonHow.com

Course Overview:
* Python - version 3
* course contains 10 real life apps
* course is divided into two sections:
  * sections 1-7 - basic Python
  * section 8 - 10 apps
    * text generator
    * web map
    * website blocker
    * static website
    * book database software
    * webcam motion detector
    * web scraper
    * data-based visualizer
    * data collector web app
    * geocoder web service

### Lecture 2 - Three Typical Python Programs

#### Command Line Interface (CLI) Application

Code is always in script file `*.py`

User starts program by typing in terminal
```
python /address/of/the/python/script/*.py
```
And then communicates with it using command line.
This type of application is best when you don't plan to distribute it to average users, who may not have Python installed or don't know how to use it.

#### Graphical User Interface (GUI) Application

Best for creating apps distributed to specific number of users, e.g. employees of the company.
It is possible to create executable file (e.g. `*.exe` for Windows, `*.app` for Mac etc.)

#### Web Application

Best for large base of users who need fast access to specific tool.

### Lecture 3 - Setting up Python on Windows

1. Download Python 3 (Python 2 will not be supported since 2020)
    * it's possible to have multiple installations of python on you machine - you can access them using appropriate shebang line in your script (or other method, but this is the most recommended)
1. Install Python
1. Add Python localization to PATH environment variable
1. Acces Python Interactive Shell from command line by typing in `python`

### Lecture 4 - Setting up Python on Mac

1. Type `python` in terminal (it's installed by default, but it's currently 2.7 version)
1. Exit it
1. Download 3.6 installator
1. Do not uninstall 2.7
1. Install 3.6
1. Type `python3`

### Lecture 5 - Creating and Executing a Python Program on Windows

`code`

Create text file with `.py` extension named `myprogram.py` which contains:
```
print("Hello")
```
Execute it in terminal using `python myprogram.py`

### Lecture 6 - Creating and Executing a Python Program on Mac

The same way as on Windows

### Lecture 7 - Setting up Atom on Windows

1. Download it from atom.io
1. Install it
1. Verify if `Show in file context menus` and `Show in folder context menus` settings options are checked
1. Install platformio-ide-terminal package for easy CMD access

### Lecture 8 - Setting up Atom on Mac

The same way as on Windows

### Lecture 9 - Installation FAQs

Skipped

## Section 2 - Variables, Datatypes, and Functions

### Lecture 10 - Section introduction

This section covers Variables and Datatypes

### Lecture 11 - Variables

`code`

Variable naming rules
* can contain letters, underscore and/or numbers
* can start with letter or underscore
* can't start with number

`input()` is a function collecting input from the users as string

```
greeting = input("Write a greeting: ")
print(greeting)
```
`int()` and `str()` are converting functions, `int()` converts floats to integers rounding them to the floor

Will collect and print out input from the user

### Lecture 12 - Numbers

`code`

You can store numbers in variables and perform mathematical operations on them using operators

`type()` is a function returning class of given object e.g.

```
print(type(2))
```
```
<class 'int'>
```
### Lecture 13 - Numbers and operators

Order of operations in Python is _PEMDAS_ (M&D and A&S are pairs on the same level, operations of the same level are being executed in left to right order)

Number solution of every mathematical equation in Python 3.6 is float

### Lecture 14 - Strings

`code`

Strings have methods associated with them, e.g.

`string.replace(a,b,n)` replaces a char with b char in given string n of times

To display all methods available for class, type `dir(class)` in Python shell

To get help about given method, type `help(class.method)` in Python shell

### Lecture 15 - String Indexing and Splitting

Each string char has index starting from 0, and reverse index starting from -1

To access substring of given string use `c[x,y]` where x is beginning index, and y is ending index excluded. In case when y<=x ^ |x+y|<n where n is length of given string, indexing returns empty substring.

Shortcuts for indexing:

`string[:3]` - everything up to index 2. character

`string[3:]` - everything since 3. character to the end of the string

### Lecture 16 - Lists

Lists
* sequences of objects from various classes
* created with __[]__ (square brackets)
* indexed the same way as Strings

To define a list (declare + initialize):
```
c = ["H",2,"Hello"]
```
`list.append` method adds object at the end of the list

`list.remove` removes object from the list

### Lecture 17 - How to ask a Good Programming Question

1. Do some research before asking a question
2. Ask on dedicated forums or StackOverflow
3. Your question should contain
  * full code you are using
  * expected behavior description
  * full error you are getting

### Lecture 18 - Tuples

Tuples
* are immutable and thus used in very specific scenarios
* are created using parentheses __()__

### Lecture 19 - Dictionaries

Dictionaries
* are created with curly brackets __{}__
* indexes are created manually not automatically
* values of dictionaries can be any class (also list, tuple, etc.)

To define a dictionary
```
list = {"key":"value", <other key-value pairs>}
```

To extract a value
```
list["key"]
```

### Quiz 1 | 4 Questions

Done in 2 approaches
1. 3/4 correct answers
2. 4/4 correct answers

### Lecture 20 - Functions

`code`

Python contains built-in functions, user can install libraries containing custom functions or create custom function himself

Indentation in function body has to be at least one space

To define a function
```
def function_name(argument1,argument_n)
  result=argument1*argument_n
  return result
```

## Section 3 - Conditionals

### Lecture 21 - Introduction

Functions - small chunks of code that help developer organize a program

Conditionals - let program make decision

### Lecture 22 - Functions - The basics

`code`

### Lecture 23 - Functions - Advanced features

`code`

To create default value for an argument
```
def function_name(argument2, argument2=default_value)
  result=argument1*argument_2
  return result
```

Argument with default value has to be placed after argument without default value
Default value can be overwritten while calling a function

`print()` can be used used instead of `return`, but it's not recommended unless it's required

### Lecture 24 - Functions and User input

`code`

### Lecture 25 - About the Exercises

Do them by yourself

### Lecture 26 and 27 - Coding Exercise 1

`code`

Exercise: Create a function that converts Celsius degrees to Fahrenheit.

My solution
```
def celcius_to_fahrenheit(celcius):
    fahrenheit = float(celcius) * 1.8 + 32
    return fahrenheit

fahrenheit = celcius_to_fahrenheit(input("Type celcius temperature: "))

print(fahrenheit)
```

Course solution
```
def c_to_f(c):
    f=c*9/5+32
    return f
print(c_to_f(10))
```

### Lecture 28 and 29 - Coding Exercise 2

Try to print out number 10 only from the following dictionary

```
money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
```

Solution

```
print(money["under_bed"][1])
```

### Lecture 30 - Conditionals

`code`

Conditionals perform different actions whether condition evaluates to be true or false

if...elif...else Conditional
```
if condition1:
  action1
elif condition2:
  action2
else :
  action3
```

### Lecture 31 - Conditionals - Advanced

`code` - uses conditional and user-defined function

### Lecture 32 and 33 - Coding Exercise 3

In exercise 1 you created a function that converted Celsius degrees to Fahrenheit.

The lowest possible temperature that physical matter can reach is -273.15 °C. With that in mind, please improve the function by making it print out a message in case a number lower than -273.15 is passed as input when calling the function.

My solution
```
def celcius_to_fahrenheit(celcius):
    if float(celcius) < -273.15:
        return "It's too low"
    else:
        fahrenheit = float(celcius) * 1.8 + 32
        return fahrenheit

fahrenheit = celcius_to_fahrenheit(input("Type celcius temperature: "))

print(fahrenheit)
```

Course solution
```
def c_to_f(c):    
    if c< -273.15:        
        return "That temperature doesn't make sense!"    
    else:        
        f=c*9/5+32        
        return f
print(c_to_f(-273.4))
```
### Lecture 34 - Loops

Loop is a way to execute a statement number of times

Python uses two types of loops:
* for
* while

### Lecture 35 - The For Loop

`code`

Usually iterates over array and applies an operation on each of it's items

To print all elements of an array:
```
for item in array:
  print(item)
```

### Quiz 2 | 4 Questions

Done in 2 approaches
1. 1/4 correct answers
2. 4/4 correct answers

### Lecture 36 - User input

`code`

User input allows program to interact with User

It's implemented through `input()` function

To store user input
```
input=input("Type input: ")
```


### Lecture 37 - While Loops

`code`

Syntax
```
while (condition):
  operations
```

### Lecture 38 - For Loop with multiple Lists

To merge two arrays use `zip(array1, array_n)` function

### Lecture 39 and 40 - Coding Exercise 4

Consider the following list:
```
temperatures=[10,-20,-289,100]
```
Then, iterate over the temperature converter function that you created in execise 3 and print out the following output.
```
50.0
-4.0
That temperature doesn't make sense!
212.0
```

My solution
```
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
```

Course solution
```
temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c > -273.15:
        f=c*9/5+32
        return f
    else:
        return "That temperature doesn't make sense!"
for t in temperatures:
    print(c_to_f(t))
#If your version looked like below, that's still correct:
temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
for t in temperatures:
    print(c_to_f(t))
```

## Section 5 - File Handling

### Lecture 41 - Introduction to File Handling
