import glob2
import datetime
import time

fileNames = glob2.glob('*.txt')

#my answer

x=''

for f in fileNames:
    with open(f, 'r+') as file:
        x += file.read() + '\n'

with open (datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt",'w') as file:
    file.write(x)

time.sleep(0.05)
#solution

filenames=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")