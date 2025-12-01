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
    addition = (1 if number > 0 else -1)
    for _ in range(abs(number)):
        total += addition
        if total > 99:
            total = total - 100
        elif total < 0:
            total = 100 + total
        if total == 0:
            zero_position += 1

print(zero_position)


# An older attempted solution below
#
# old_total = total
# total += number
# if old_total // 100 != total // 100:
#     zero_position += abs((old_total // 100) - (total // 100))
#     print(old_total, total)
# total %= 100