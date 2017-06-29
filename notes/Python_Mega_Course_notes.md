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

This section Variables and Datatypes

### Lecture 11 - Variables

Variable naming rules
* can contain letters, underscore and/or numbers
* can start with letter or underscore
* can't start with number
