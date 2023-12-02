with open('input.txt', 'r') as f:
    lines = f.readlines()
    res = 0
    digit_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for l in lines:
        digits = []
        for i, c in enumerate(l):
            if c.isdigit():
                digits.append(c)
            for v, name in enumerate(digit_names):
                if l[i:].startswith(name):
                    digits.append(str(v + 1))
                
        res += int(digits[0] + digits[-1])
        
    print(res)
    