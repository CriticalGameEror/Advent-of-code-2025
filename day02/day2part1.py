import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readline()
    input_text = input_text.split(",")

total = 0
for num_range in input_text:
    num_min, num_max = num_range.split("-")
    for x in range(int(num_min), int(num_max)+1):
        temp_str = str(x)
        # ID will only be invalid if it has an even length
        if len(temp_str) % 2 == 0:
            if temp_str[:int(len(temp_str)/2)] == temp_str[int(len(temp_str)/2):]:
                total += x

print(total)