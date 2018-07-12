from polymino import generate_all, Grid, PENTOMINOES, solutions_svg, unique_grids
from dlx import DLX

def sortkey(x):
    x = str(x)
    return (len(x), x)

COLOURS = dict(I="#EEAAAA", F="#DDBB99", L="#CCCC88",
               P="#BBDD99", N="#AAEEAA", T="#99DDBB",
               U="#88CCCC", V="#99BBDD", W="#AAAAEE",
               X="#BB99DD", Y="#CC88CC", Z="#DD99BB")

# Grid for Scott's pentomino problem: 8x8 with a 2x2 hole in the middle
GRID = Grid((8, 8), holes=[(3, 3), (3, 4), (4, 3), (4, 4)])

# Generate all pentominoes that can be placed on the grid
POLYMINOES = generate_all(PENTOMINOES, GRID)

# convert to list of lists
POLYMINOES = [polymino.aslist for polymino in POLYMINOES]

# calculate labels for DLX 
LABELS = list(set([element for polymino in POLYMINOES for element in polymino]))
LABELS = sorted(LABELS, key=sortkey)

COVER = DLX(LABELS, POLYMINOES)

SOLUTIONS = []
for i, SOLUTION in enumerate(COVER.generate_solutions()):
    print(i)
    SOLUTIONS.append(Grid.from_DLX(SOLUTION))

DISTINCT_SOLUTIONS = unique_grids(SOLUTIONS)

solutions_svg(DISTINCT_SOLUTIONS, filename='scott_distinct_solutions1.svg',
              columns=13, colour=COLOURS.get)

# removing X pentominoes
POLYMINOES = [pol for pol in POLYMINOES if not (pol[0] == 'X' and pol[1] not in [(5, 3), (5, 2), (4, 2)])]

COVER = DLX(LABELS, POLYMINOES)

SOLUTIONS = []
for i, SOLUTION in enumerate(COVER.generate_solutions()):
    print(i)
    SOLUTIONS.append(Grid.from_DLX(SOLUTION))

DISTINCT_SOLUTIONS = unique_grids(SOLUTIONS)

solutions_svg(DISTINCT_SOLUTIONS, filename='scott_distinct_solutions2.svg',
              columns=13, colour=COLOURS.get)
