grid = []
word = 'XMAS'

with open(r'C:\Users\jshap\OneDrive\Desktop\input4.txt', 'r') as f:
    for line in f:
        grid.append(line[0:-1])

rows = len(grid)
cols = len(grid[0])
size = len(word)
count = 0

directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
        (-1, -1), # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1)    # down-right
    ]

def match(r, c, dr, dc):
        for i in range(size):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols):  # Out of bounds
                return False
            if grid[nr][nc] != word[i]:  # Mismatch
                return False
        return True

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            if match(r, c, dr, dc):
                count += 1

print(count)