import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("executable", type=str)
parser.add_argument("parameter", type=str, nargs='*')
args = parser.parse_args()

executable = args.executable

cmd = ""
cmd += "./" + executable + " "
for parameter in args.parameter:
    cmd += parameter + " "

os.system("rm stats.txt")
for i in range(1):
    os.system("perf stat -o stats.txt --append " + cmd)

bytesMemoryString = ""
for i in range(1):
    os.system("rm memstatstmp.txt")
    os.system("strace -r -e read,write -o memstatstmp.txt " + cmd)
    bytesMemory = 0
    with open("memstatstmp.txt", "r") as stats:
        while True:
            line = stats.readline()
            print(line)
            if len(line.split("=")) == 2:
                bytesMemory += int(line.split("=")[1].strip())
            if not line:
                break
    bytesMemoryString += str(bytesMemory) + ","

os.system("rm memstats.txt")
with open("memstats.txt", "w") as stats:
    stats.write(bytesMemoryString[0:-1])
