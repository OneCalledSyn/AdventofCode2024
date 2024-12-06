import re

pattern = r"mul\(\d{1,3},\d{1,3}\)"
terms = []

with open(r'C:\Users\jshap\OneDrive\Desktop\input3.txt', 'r') as f:
    for line in f:
        matches = re.findall(pattern, line)
        if matches:
            terms.extend(matches) 

total = 0

for i in range(len(terms)):
    nums = terms[i][4:-1].split(',')
    total += int(nums[0]) * int(nums[1])

print(total)

# Part 2
                  
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
terms = []

with open(r'C:\Users\jshap\OneDrive\Desktop\input3.txt', 'r') as f:
    for line in f:
        matches = re.findall(pattern, line)
        if matches:
            terms.extend(matches) 

total = 0
process = True

for i in range(len(terms)):

    if terms[i][0:3] == 'mul' and process == True:
        nums = terms[i][4:-1].split(',')
        total += int(nums[0]) * int(nums[1])
    
    if terms[i] == "do()":
        process = True

    if terms[i] == "don't()":
        process = False

print(total)