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
        # For each set
        for p in parsed:
            p = p.strip().split(',')
            for num_col in p:
                num_col = num_col.strip().split(' ')
                num = int(num_col[0])
                col = num_col[1]
                if col == 'red' and num > RED:
                    valid = False
                    break
                if col == 'green' and num > GREEN:
                    valid = False
                    break
                if col == 'blue' and num > BLUE:
                    valid = False
                    break
            if valid == False:
                break
            
        if valid:
            res += i+1
    print(res)
    