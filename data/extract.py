from time import sleep


cycles = ""
with open("stats.txt", "r") as stats:
    while True:
        line = stats.readline()
        if "cycles" in line:
            cyclesstripped = line.split("cycles")[0].strip().replace(",", "")
            cycles += cyclesstripped + ","
        if not line:
            break
bytesMemory = ""
with open("memstats.txt", "r") as stats:
    bytesMemory = stats.readline()
print("Demand:" + "CPU:" + cycles[0:-1] + ";" + "HDD:" + bytesMemory)
