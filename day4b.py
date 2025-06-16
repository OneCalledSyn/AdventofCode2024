# grid = []
# word = 'MAS'

# with open(r'C:\Users\jshap\OneDrive\Desktop\input4.txt', 'r') as f:
#     for line in f:
#         grid.append(line[0:-1])

def count_x_shapes(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    x_count = 0

    # Check if the given center (r, c) forms an "X"
    def is_x_center(r, c):
        # The center must match the second letter of the word
        if grid[r][c] != word[1]:
            return False

        # Check for "MAS" in two diagonals
        def matches_diagonal(dr, dc):
            for i in range(word_len):
                nr, nc = r + dr * i, c + dc * i
                if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                    return False
            return True

        # Check up-left and down-right
        diag1 = matches_diagonal(-1, -1) and matches_diagonal(1, 1)
        # Check up-right and down-left
        diag2 = matches_diagonal(-1, 1) and matches_diagonal(1, -1)

        return diag1 and diag2

    # Iterate through all possible centers
    for r in range(rows):
        for c in range(cols):
            if is_x_center(r, c):
                x_count += 1

    return x_count

# Example Grid
grid = [
    ['M', 'A', 'M', 'A', 'M'],
    ['A', 'S', 'A', 'S', 'A'],
    ['M', 'A', 'M', 'A', 'M'],
    ['A', 'S', 'A', 'S', 'A'],
    ['M', 'A', 'M', 'A', 'M']
]

word = "MAS"

x_count = count_x_shapes(grid, word)
print(f"The number of 'X' shapes formed by '{word}' is: {x_count}")