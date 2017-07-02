r"""
This script creates an empty file, this will display additional breakline symbols
"""
import datetime

filename="..\\output\\Lecture_52_output_"+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")+".txt"

#create empy file

def create_file():
    """This function creates an empty file"""
    with open(filename,"w") as file:
        file.write("") # writing empty string
        file.close()

create_file()
