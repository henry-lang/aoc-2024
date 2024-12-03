import re

DO = 1
DONT = 2

def part_a(input: str):
    pattern = r"mul\(\d+,\d+\)"

    # Find all matches
    matches = re.findall(pattern, input)
    t = 0

    for m in matches:
        m = m.replace("mul(", "").replace(")", "")
        a, b = m.split(",")
        t += int(a) * int(b)

    return t

def part_b(input: str):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.finditer(pattern, input)

    pattern_do = r"do\(\)"
    pattern_dont = r"don't\(\)"

    all_do = list(map(lambda m: (DO, m.start()), re.finditer(pattern_do, input)))
    all_dont = list(map(lambda m: (DONT, m.start()), re.finditer(pattern_dont, input)))
    all = sorted([(DO, 0)] + all_do + all_dont, key=lambda x: x[1])

    t = 0

    for m in matches:
        start = m.start()
        *_, first = filter(lambda n: start > n[1], all)

        if first[0] == DO:
            m = m.group().replace("mul(", "").replace(")", "")
            a, b = m.split(",")
            t += int(a) * int(b)
    
    return t
