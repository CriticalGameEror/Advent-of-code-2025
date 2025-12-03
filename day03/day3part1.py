import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readlines()

total = 0
for bank in input_text:
    bank = bank.strip()
    highest1 = 0
    highest2 = 0
    for i, battery in enumerate(bank):
        if int(battery) > highest1:
            # the highest cannot be updated in the case below since it would break the rules
            if i == len(bank)-1:
                highest2 = max(highest2, int(battery))
                continue
            highest1 = int(battery)
            highest2 = 0 # reset highest2 because this number will always be higher
        elif int(battery) > highest2:
            highest2 = int(battery)
    print(int(str(highest1) + str(highest2)))
    total += int(str(highest1) + str(highest2))

print(total)
