counter_dict = {}
with open('names.txt') as namesTotal:
    line = namesTotal.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = namesTotal.readline()

print(counter_dict)
