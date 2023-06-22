path = input()

with open(path) as file:
    lines = file.read().splitlines()
    for i, line in enumerate(lines, start=1):
        if len(line) > 79:
            print(f'Line {i}: S001 Too long')
