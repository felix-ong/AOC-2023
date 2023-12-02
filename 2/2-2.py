# For each game, for each set, parse into number of red, green and blue, if any exceeds, invalid.
# If not exceed, add id (line number + 1)
RED = 12
GREEN = 13
BLUE = 14

with open('input.txt', 'r') as f:
    lines = f.readlines()
    res = 0
    # For each game
    for i, l in enumerate(lines):
        parsed = l.split(':')[1].split(';')
        valid = True
        max_red = 0
        max_green = 0
        max_blue = 0
        # For each set
        for p in parsed:
            p = p.strip().split(',')
            for num_col in p:
                num_col = num_col.strip().split(' ')
                num = int(num_col[0])
                col = num_col[1]
                if col == 'red':
                    max_red = max(max_red, num)
                elif col == 'green':
                    max_green = max(max_green, num)
                elif col == 'blue':
                    max_blue = max(max_blue, num)
        res += max_red * max_green * max_blue
    print(res)
    