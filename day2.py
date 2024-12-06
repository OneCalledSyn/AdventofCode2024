safe = 0

with open(r'C:\Users\jshap\OneDrive\Desktop\input2.txt', 'r') as f:
    for line in f:
        levels = line.split()
        n = len(levels)
        increasing = all(int(levels[i]) < int(levels[i + 1]) for i in range(n - 1))
        decreasing = all(int(levels[i]) > int(levels[i + 1]) for i in range(n - 1))
        gradual = all(abs(int(levels[i]) - int(levels[i + 1])) in (1, 2, 3) for i in range(n - 1))

        if gradual and (increasing or decreasing):
            safe += 1

print(safe)

# Part 2

mostly_safe = 0

with open(r'C:\Users\jshap\OneDrive\Desktop\input2.txt', 'r') as f:
    for line in f:
        levels = line.split()
        n = len(levels)

        def check(levels):
            increasing = all(int(levels[i]) < int(levels[i + 1]) for i in range(len(levels) - 1))
            decreasing = all(int(levels[i]) > int(levels[i + 1]) for i in range(len(levels) - 1))
            gradual = all(abs(int(levels[i]) - int(levels[i + 1])) in (1, 2, 3) for i in range(len(levels) - 1))

            return gradual and (increasing or decreasing)
        
        if check(levels):
            mostly_safe += 1
        
        else:
            for i in range(n):
                remove_one = levels[:i] + levels[i + 1:]
                if check(remove_one):
                    mostly_safe += 1
                    break

print(mostly_safe)