import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readlines()
    for index, item in enumerate(input_text):
        input_text[index] = int(item.strip().replace("R", "+").replace("L", "-"))


zero_position = 0
total = 50
for number in input_text:
    total = (total + number) % 100
    if total == 0:
        zero_position += 1

print(zero_position)
