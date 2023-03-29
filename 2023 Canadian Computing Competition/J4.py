num_columns = int(input())
first_line = input().split()
second_line = input().split()
tape_needed = 0

for col in range(num_columns):
    if first_line[col] == '1':
        tape_needed += 3
        if col < num_columns - 1 and first_line[col + 1] == '1' or second_line[col] == '1' and col % 2 == 0:
            tape_needed -= 2

    if second_line[col] == '1':
        tape_needed += 3
        if col < num_columns - 1 and second_line[col + 1] == '1':
            tape_needed -= 2

print(tape_needed)