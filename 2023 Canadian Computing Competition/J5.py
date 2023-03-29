word = input()
num_rows = int(input())
num_cols = int(input())
grid = [''.join(input().split()) for _ in range(num_rows)]
total_count = 0

def check_line(row):
    if word[::-1] == word:
        return row.count(word)
    else:
        return row.count(word) + row[::-1].count(word)

def check_vertical(col_id):
    col = ""
    for row in grid:
        col += row[col_id]
    
    return check_line(col)

def check_lu_diagonal(row_id, col_id):
    diagonal = ""
    while row_id >= 0 and col_id >= 0:
        diagonal += grid[row_id][col_id]
        row_id -= 1
        col_id -= 1
    return check_line(diagonal)

def check_ru_diagonal(row_id, col_id):
    diagonal = ""
    while row_id >= 0 and col_id < num_cols:
        diagonal += grid[row_id][col_id]
        row_id -= 1
        col_id += 1
    return check_line(diagonal)

def check_ld_diagonal(row_id, col_id):
    diagonal = ""
    while row_id < num_rows and col_id >= 0:
        diagonal += grid[row_id][col_id]
        row_id += 1
        col_id -= 1
    
    return check_line(diagonal)

def check_rd_diagonal(row_id, col_id):
    diagonal = ""
    while row_id < num_rows and col_id < num_cols:
        diagonal += grid[row_id][col_id]
        row_id += 1
        col_id += 1
    
    return check_line(diagonal)

def check_diagonal(row_id, col_id):
    diagonal1 = check_lu_diagonal(row_id, col_id)
    diagonal2 = check_ru_diagonal(row_id, col_id)
    diagonal3 = check_ld_diagonal(row_id, col_id)
    diagonal4 = check_rd_diagonal(row_id, col_id)

    return diagonal1 + diagonal2 + diagonal3 + diagonal4

# checks for horizontal words
for row_id, row in enumerate(grid):
    total_count += check_line(row)

    # checks for diagonal words
    for col_id, char in enumerate(row):
        if char == word[0]:
            total_count += check_diagonal(row_id, col_id)

# checks for vertical words
for col_id in range(num_cols):
    total_count += check_vertical(col_id)

print(total_count)
