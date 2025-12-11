import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readlines()

ranges = []
ingredients = []
reached_ingredients = False
for line in input_text:
    line = line.strip()
    if line == "":
        reached_ingredients = True
        continue
    if not reached_ingredients:
        ranges.append(line)
    else:
        ingredients.append(int(line))

total = 0
for ingredient in ingredients:
    for i in ranges:
        start_numb, end_numb = i.split("-")
        if int(start_numb) <= ingredient <= int(end_numb):
            total += 1
            break
print(total)
