left, right = [], []

with open(r'C:\Users\jshap\OneDrive\Desktop\input1.txt', 'r') as f:
    for line in f:
        halves = line.split()
        left.append(halves[0])
        right.append(halves[1])
     
left.sort()
right.sort()

total = 0

for i in range(len(left)):
    total += abs(int(left[i]) - int(right[i]))

print(total)

similarity = 0

for elt in left:
    similarity += right.count(elt) * int(elt)

print(similarity)
