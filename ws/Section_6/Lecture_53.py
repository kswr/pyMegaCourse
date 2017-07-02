import glob2
import datetime

input=glob2.glob("..\\input\\Lecture_53_data\\*")

output="..\\output\\Lecture_53_output_"+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"

# replace opening and closing operations to generate less O

for i in input:
    with open(i, 'r') as file:
        with open(output, 'a') as file_2:
            file_2.write(file.read()+"\n")
