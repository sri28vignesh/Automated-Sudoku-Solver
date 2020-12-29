from itertools import product

def algorithmx(size, grid):
    """ An efficient Sudoku solver using Algorithm X."""
    R, C = size
    N = R * C
    X = ([("rc", rc) for rc in product(range(N), range(N))] +
        [("rn", rn) for rn in product(range(N), range(1, N + 1))] +
        [("cn", cn) for cn in product(range(N), range(1, N + 1))] +
        [("bn", bn) for bn in product(range(N), range(1, N + 1))])
    Y = dict()
    for r, c, n in product(range(N), range(N), range(1, N + 1)):
        b = (r // R) * R + (c // C) # Box number
        Y[(r, c, n)] = [
            ("rc", (r, c)),
            ("rn", (r, n)),
            ("cn", (c, n)),
            ("bn", (b, n))]
    X, Y = exact_cover(X, Y)
    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            if n:
                select(X, Y, (i, j, n))
    for solution in solve(X, Y, []):
        for (r, c, n) in solution:
            grid[r][c] = n
        yield grid

def exact_cover(X, Y):
    X = {j: set() for j in X}
    for i, row in Y.items():
        for j in row:
            X[j].add(i)
    return X, Y

def solve(X, Y, solution):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()

def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)

def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False
  return True

#Backtracking algorithm
def backtracking(grid):

  for i in range(0,81):
    row=int(i/9)
    col=int(i%9)
    if grid[row][col]==0:
      for value in range (1,10):
        if not(value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:
                square=[grid[i][6:9] for i in range(6,9)]
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if checkGrid(grid):
                return grid
              else:
                  if solveGrid(grid):
                    return grid
      break
  grid[row][col]=0