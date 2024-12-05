def parse(input: str):
    a, b = input.split("\n\n")
    rules = [tuple(map(int, x.split("|"))) for x in a.split("\n")]
    orig = [list(map(int, x.split(","))) for x in b.split("\n")]

    updates = []
    for orig_update in orig:
        update = ({}, orig_update)
        for i, u in enumerate(orig_update):
            update[0][u] = i
        updates.append(update)

    return rules, updates

def part_a(input: str):
    rules, updates = parse(input)
    total = 0

    for u, orig in updates:
        invalid = False
        for a, b in rules:
            if invalid == True:
                 break

            if a in u and b in u and not u[a] < u[b]:
                invalid = True
        if not invalid:
            total += orig[len(orig) // 2]

    return total

def part_b(input: str):
    rules, updates = parse(input)
    total = 0

    for u, orig in updates:
        invalid = False
        for a, b in rules:
            if a in u and b in u and not u[a] < u[b]:
                invalid = True
                orig[u[a]], orig[u[b]] = orig[u[b]], orig[u[a]]
                u[a], u[b] = u[b], u[a]
        if invalid:
            while invalid:
                invalid = False
                for a, b in rules:
                    if a in u and b in u and not u[a] < u[b]:
                        invalid = True
                        orig[u[a]], orig[u[b]] = orig[u[b]], orig[u[a]]
                        u[a], u[b] = u[b], u[a]
            total += orig[len(orig) // 2]

    return total