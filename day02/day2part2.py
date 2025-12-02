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
        # Edge case when the number is all the same digit, also check for length 1 IDs, which can't be invalid
        if temp_str.count(temp_str[0]) == len(temp_str) and len(temp_str) != 1:
            total += x
            continue
        # Start at 2 because 1 is already handled above
        for seq_length in range(2, (len(temp_str)//2) + 1):
            occurances = temp_str.count(temp_str[:seq_length])
            # Need to check that the length of the substring multiplied by the occurance is equal to the length of the full string
            if len(temp_str[:seq_length]) * occurances == len(temp_str):
                if occurances == 1:
                    # All invalid IDs with repeated sequences of length 1 are already handled above
                    continue
                total += x
                break

print(total)