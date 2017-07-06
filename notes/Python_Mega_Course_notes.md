# [Python Mega course](https://www.udemy.com/the-python-mega-course/learn/v4/overview)

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
## Section 4 - Loops and User input

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

For loop wrapped in square brackets
```
list_copy = [i for i in list]
```
Copies list `list` elements to `list_copy` list object

```
content=[i.rstrip("\n") for i in content]
```
Removes new line symbol from all elements of `content` list object

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

Python can read content of the files, this section will cover this topic

### Lecture 42 - Opening and Reading a File

`input`

To open a file use `open()` method, which passes file contents to file wrapper variable
```
file_in_python=open("your_file.txt",'mode')
```
The most important modes of `open()` method are
* `r` - read - reads the file
* `w` - write - overwrites the file
* `a` - append - appends to the file

`open()` method creates object of `_io.TextIOWrapper` class (file object)

To read content of the file use `file.read()` method and store it in a variable
```
content=file_in_python.read()
```

Or `file.readlines()` to store content in a list
```
contentlist=file_in_python.readlist()
```

__Pointer__ - when Python opens the file, pointer is placed at it's beggining. Reading operation moves pointer over following elements of the file to it's end. To perform new operations on file's contents, pointer has to be moved to desired position using `.seek()` method.

To move pointer to beggining of the file
```
file_in_python.seek(0)
```

To remove given characters from string, use `str.rstrip()` method
```
S.rstrip([chars]) -> str
```
Return a copy of the string S with trailing whitespace removed.
If chars is given and not None, remove characters in chars instead.

If file is modified and not closed in Python, the changes are not written to this file.
Always apply `file_in_python.close()` method.

### Lecture 43 - Opening and Writing Text to a Text File

`input`

To create a file, use `open()` method with `w` parameter
```
file=open("Non_existing_yet_file.txt","w")
```

To write to a file use `write()` method
```
file.write("String of content")
```

To write a line and go to the next one use new line symbol
```
file.write("Line 1 content\n")
```
Remember to close the file with `file.close()` method

To concatenate strings use `+` operator

### Lecture 44 - Appending to a File

`input`

Open file with argument `a` - append
```
file=open("filename",'a')
```
### Lecture 45 - The Rest of File Handling methods

* `r+` - opens file for both reading and writing (places pointer at the beginning of the file)
* `w+` - opens file for both writing and reading (overwrites existing file, which implies placing pointer at the beginning of the file)
* `a+` - opens file for both appending and reading (places pointer at the end of the file)

### Lecture 46 - The "with" Statement

`input`

* helps you writing clean code when working with files
* makes sure file is closed after performing operations on it

Example:
```
with open("File.txt",'a+') as file:
  # move pointer to the beggining of the file
  file.seek(0)
  # global variable
  content=file.read()
  # new line
  file.write("\nLine21")
```

## Section 6 - More Functionalities

### Lecture 49 - Introduction

This section covers
* external libraries
* dates
* commenting
* documenting
* other

### Lecture 50 - Modules, Libraries and Packages

Python is installed by default with built-in functions, which load into memory with Python

There are also additional libraries and modules which can be loaded using keyword `import()`

__Module__ - Python file with custom functions

To check path of module use `module.__file__` method

__Library__ - Collection of modules

__Packages__ - 3rd party Libraries and Modules

__pip__ - Pip Installs Packages; package management system used to install and manage software packages written in Python

To install package (use it outside Python interactive shell)
```
pip install packagename
```
To install local package (e.g. precompiled `*.whl` file)
```
pip install /directory/to/file.whl
```

__PyPI__ - Python Package Index; most of packages can be found here

### Lecture 51 - Commenting and Documenting your code

`code`

To type one-line comment
```
# one-line comment
```
There are no multiline comments in Python

Docstrings - to access docstring use `package.__doc__` method

To create docstring
```
r"""
Content of the docstring, e.g. "This script creates an empty file"
"""
```
`r` before docstring escapes special symbols in docstring

### Lecture 52 - Dates and Times

`code`

Most important built-in modules
* `datetime`
* `date`

#### `datetime`

Get current time in 24h system (datetime.datetime object) depending on current computer time
```
datetime.datetime.now()

# moudule.class.method
```
`datetime` converts to readable string


To get difference between given time and current moment
```
yesterday=datetime.datetime(2017,6,30,11,0,0,0)
now=datetime.datetime.now()
diff=now-yesterday
```
Variable `diff` stores now `timedelta` object of `datetime` instance, which is an array storing `(day, seconds, microseconds)`

`timedelta` class most commonly used methods
* `.days` - returns total days from delta
* `.total_seconds` - returns total seconds from delta

`strftime()` method of datetime.datetime instance, which allows user to style string

Example, to get current year
```
datetime.datetime.now().strftime("%Y")
```
Output
```
'2017'
```

To add period of time to `datetime.datetime` instance object, use `datetime.delta` class object
```
now_in_two_days=datetime.datetime.now()+datetime.delta(days=2)
```

`time` module - good for managing time in operations performed by Python

Example
```
# this loop will append one element of datetime.datetime instance to lst list every second

lst=[]
for i in range(5):
  lst.append(datetime.datetime.now())
  time.sleep(1)
```

### Lecture 53 to 55 - Coding Exercise 6

`code` `input`

Please download the ZIP file in the Resources and unzip it in a folder.

Then create a script that merges the three text files into a new text file containing the text of all three files. The filename of the merged text file should contain the current timestamp down to the millisecond level. E.g. "2016-06-01-13-57-39-170965.txt".

My solution
```
import glob2
import datetime

input=glob2.glob("..\\input\\Lecture_53_data\\*")

output="..\\output\\Lecture_53_output_"+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"

# replace opening and closing operations to generate less O

for i in input:
    with open(i, 'r') as file:
        with open(output, 'a') as file_2:
            file_2.write(file.read()+"\n")
```

Course solution
```
import glob2
import datetime

filenames=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")
```

## Section 7 - Application 1: Building a Text Generator

### Lecture 56 - Introduction

Application built in this section is simple text generator, it requires knowledge of the following concepts:
* Variables
* Functions
* Conditionals
* User input
* For Loops

### Lecture 57 - Demonstration of the Text Generator Application

`code`

Program generates 10 random 3-char strings, user type of characters in strings as vowels or consonants

### Lecture 58 - Building Version 1

`code`

`string` module contains methods for operating on strings

`string.ascii_lowercase` method contains lowercase ascii alphabet

`random.choice` chooses random element from non-empty sequence

### Lecture 59 - Building Version 2

`code`

My version of code in file `Application_1_my_version.py`

### Lecture 60 - Building Version 3

Author adds loop to his version of code

## Section 8 - Data Analysis with Pandas

### Lecture 61 - What is Pandas?

`pandas` is Python library providing data structures and data analysis tools (recommended library for visualizing data is `bokeh`) based on `numpy` library

It can be used for
* web data scrapping
* loading data
* analyzing data

To install (from OS command shell)
```
pip install pandas
```

### Lecture 62 - Getting Started with Pandas

__IPython__ - command shell for interactive computing in multiple programming languages, originally developed for the Python programming language, that offers introspection, rich media, shell syntax, tab completion, and history. IPython provides the following features
* Interactive shells (terminal and Qt-based).
* A browser-based notebook with support for code, text, mathematical * expressions, inline plots and other media.
* Support for interactive data visualization and use of GUI toolkits.
* Flexible, embeddable interpreters to load into one's own projects.
* Tools for parallel computing.

In the following lectures we will use __Jupyter Notebook__

To create `pandsa.DataFrame` object
```
df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Values"],index=["First","Second"])
```
output
```
        Price  Age  Values
First       2    4       6
Second     10   20      30
```

Example 2
```
df2 = pandas.DataFrame([{"Name":"John","Surname":"Johns"},{"Name":"Jack"}])
```

Output
```
   Name Surname
0  John   Johns
1  Jack     NaN
```

Mean
```
df1.mean().mean() # mean for whole dataframe
df1.Price.mean # mean for one column
```
### Lecture 63 - Getting Started with Jupyter notebook

Jupyter is tool for
* working with data analysis
* testing code
* testing visualization code
* web scrapping (using e.g. BeautifullSoup )
* other

Jupyter can be installed through `pip`

Jupyter has 2 modes
* insert mode
* command mode (command similar to vim commands)

Keyboard shortcuts in Jupyter are available through `Help` -> `Keyboard shortcuts`

### Lecture 64 - Loading Data in Python from CSV, Excel, TXT and JSON Files

`jupyter`

### Lecture 65 - Indexing and Slicing Dataframes

`jupyter`

### Lecture 66 - Dropping Dataframe Columns and Rows

`jupyter`

### Lecture 67 - Updating and Adding new Columns and Rows

`jupyter`

### Lecture 68 - Example: Geocoding Addresses with Pandas and Geopy

`jupyter`

## Section 9 - numpy

### Lecture 69 - What is Numpy?

`jupyter`

### Lecture 70 -  Installing OpenCV (cv2)

`jupyter`

### Lecture 71 - Images to Numpy and Vice-versa

`jupyter`

### Lecture 72 - Indexing, Slicing, and Iterating

`jupyter`

### Lecture 73 - Stacking and Splitting

`jupyter`

## Section 10 - Application 2: Creating Webmaps with Python and Folium

### Lecture 74 - Demonstration of the Web Mapping Application

Web Map
* can be displayed in web browser
* has layers
* built with Python and `folium` library

### Lecture 75 - Creating the Open Street Map (OSM) Basemap

`code`

#### folium

The most important instance of this library is object of `map` class
```
map = folium.Map
```
Map created in `folium` is automatically translated to JS, CSS and HTML, which can be read by browser

Create map object centered on Warsaw
```
map = folium.Map(location=[52.250265,21.017909])
```

### Lecture 76 - Adding a Point Marker Feature to the Map

`code`

Things that can be modified when creating a map object in `folium`
* location
* width
* height
* tiles - it can be one of default, custom or 'None' for map without tiles
* other

To add elements to map create them as `child` of map object

Markers are simple `leaflet` (JS library) objects
```
map.add_child(folium.Marker(location=[52.250265,21.017909], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
```

Layers and objects added to the folium map should be stored and grouped in feature groups
```
fg = folium.FeatureGroup(name="My Map")
fg.add_child(...)
map.add_child(fg)
```

### Lecture 77 - Adding Multiple Markers to the Map

`code`

User for loop on list of coordinates Lists
```
for coordinates in [[52.250265,21.017909],[52.550265,21.117909]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))
```

### Lecture 78 - Adding Markers from Data Files

`code`

Import data using `pandas` library

Iterate over markers location using loaded data
```
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
```

### Lecture 79 - Creating Popup Windows for Map Features

`code`

Apply for loop on popup parameter
```
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+ " m", icon=folium.Icon(color='green')))

```

### Lecture 80 - Color-Based Point Markers

`code`

Use function to define `color` parameter based on value of value assigned to it

### Lecture 81 and 82 - Coding Exercise: Adding and Styling Circle Markers

`code`

### Lecture 83 - Solution of the Coding Exercise: Adding and Styling Circle Markers

Use `folium.CircleMarker` map feature
```
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+ " m", fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

```

### Lecture 84 - Using GeoJson data

GIS systems feature
* polygons
* points
* lines

Adding polygon layers (countries with colors representing population) via `folium.GeoJson` method

`GeoJson` is special instance of `JSON` file

### Lecture 85 - Adding a GeoJson Polygon Layer

`code`

Use `folium.GeoJson`
```
fg.add_child(folium.GeoJson(data=(open('../input/Lecture_84_data/world.json', 'r', encoding='utf-8-sig'))))
```

### Lecture 86 - Color-Based Polygon Features

`code`

`lambda` function allows user to write single-line, simple functions, e.g.

```
l = lambda x: x**2
l(5)
```

To set color of the polygon based on it's value, use `lambda` in `folium.GeoJason` `style_function` parameter

```
fg.add_child(folium.GeoJson(data=open('../input/Lecture_84_data/world.json', 'r', encoding='utf-8-sig'), style_function=lambda x: {'fillColor':'green' if x ['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
```
### Lecture 87 - Adding a Layer Control Panel