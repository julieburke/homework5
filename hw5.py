import re

with open("regex_sum_31747.txt", "r") as data:
	totsum = 0
	for line in data:
		for item in re.findall("([0-9]+)", line):
			totsum += int(item)
	print (totsum)