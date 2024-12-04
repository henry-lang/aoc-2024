from collections import defaultdict


def part_a(input: str):
    grid = [x for x in input.split("\n")]
    transposed = ["".join(row) for row in zip(*grid)]

    diagonals = []
    n = len(grid)
    
    for k in range(-(n-1), n):
        diagonal = []
        for i in range(n):
            j = k + i
            if 0 <= j < n:
                diagonal.append(grid[i][j])
        if diagonal:
            diagonals.append("".join(diagonal))
            
    for k in range(2*n - 1):
        diagonal = []
        for i in range(n):
            j = k - i
            if 0 <= j < n:
                diagonal.append(grid[i][j])
        if diagonal:
            diagonals.append("".join(diagonal))
    
    count = 0
    
    # Check rows
    for row in grid:
        count += row.count("XMAS")
        count += row.count("SAMX")
    
    # Check columns 
    for col in transposed:
        count += col.count("XMAS")
        count += col.count("SAMX")
        
    # Check diagonals
    for diag in diagonals:
        count += diag.count("XMAS")
        count += diag.count("SAMX")
        
    return count

def part_b(input: str):
    grid = [x for x in input.split("\n")]
    g = defaultdict(str)
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            g[(i, j)] = grid[i][j]

    all_a = [x for x in g.keys() if g[x] == "A"]
    
    t = 0

    for r, c in all_a:
        a1 = g[(r - 1, c - 1)]
        a2 = g[(r + 1, c + 1)]
        b1 = g[(r - 1, c + 1)]
        b2 = g[(r + 1, c - 1)]

        expected = [("M", "S"), ("S", "M")]
        
        if (a1, a2) in expected and (b1, b2) in expected:
            t += 1
            
    return t
