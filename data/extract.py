cycles = "DoublePMF["
with open("stats.txt", "r") as stats:
    while True:
        line = stats.readline()
        if "cycles" in line:
            cyclesstripped = line.split("cycles")[0].strip().replace(",", "")
            cycles += "(" + cyclesstripped + ";0.01)"
        if not line:
            break
cycles += "]"
bytesMemory = "DoublePMF["
with open("memstats.txt", "r") as stats:
	for bytes in stats.readline().split(","):
		bytesMemory += "(" + bytes + ";0.01)"
bytesMemory += "]"
print("Demand:" + "CPU:" + cycles + "&" + "HDD:" + bytesMemory)
