from collections import defaultdict

def part_a(input: str):
    lines = [tuple(map(int, l.split())) for l in input.split("\n")]
    a, b = sorted([l[0] for l in lines]), sorted([l[1] for l in lines])
    t = 0

    for i, j in zip(a, b):
        t += abs(i - j)

    return t

def part_b(input: str):
    lines = [tuple(map(int, l.split())) for l in input.split("\n")]
    a, b = sorted([l[0] for l in lines]), sorted([l[1] for l in lines])
    t = 0
    f = defaultdict(int)
    for n in b:
        f[n] += 1

    for n in a:
        t += n * f[n]

    return t
