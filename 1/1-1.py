with open('input.txt', 'r') as f:
    lines = f.readlines()
    res = 0
    for l in lines:
        digits = []
        for c in l:
            if c.isdigit():
                digits.append(c)
        res += int(digits[0] + digits[-1])
        
    print(res)
    