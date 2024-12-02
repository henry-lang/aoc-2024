def parse(input: str):
    return [list(map(int, l.split())) for l in input.split("\n")]

def part_a(input: str):
    data = parse(input)
    s = 0

    for l in data:
        delta = [l[i] - l[i-1] for i in range(len(l) - 1, 0, -1)]
        s += (int(all(s < 0 for s in delta) or all (s > 0 for s in delta))) and all(1 <= abs(s) <= 3 for s in delta)

    return s

def part_b(input: str):
    data = parse(input)
    s = 0

    for l in data:
        delta = [l[i] - l[i-1] for i in range(len(l) - 1, 0, -1)]
        print(delta)
        safe = ((all(s < 0 for s in delta) or all(s > 0 for s in delta))) and all(1 <= abs(s) <= 3 for s in delta)
        for i in range(len(l)):
            l_copy = l.copy()
            l_copy.pop(i)
            delta_new = [l_copy[i] - l_copy[i-1] for i in range(len(l_copy) - 1, 0, -1)]
            safe |= ((all(s < 0 for s in delta_new) or all(s > 0 for s in delta_new))) and all(1 <= abs(s) <= 3 for s in delta_new)

        s += safe
    return s
