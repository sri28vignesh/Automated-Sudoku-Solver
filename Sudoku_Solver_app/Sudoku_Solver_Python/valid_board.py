def valid_row(row, grid):
  temp = grid[row]
  # Removing 0's.
  temp = list(filter(lambda a: a != 0, temp))
  # Checking for invalid values.
  if any(i < 0 and i > 9 for i in temp):
    #print("Invalid value")
    return -1
  # Checking for repeated values.
  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1
# Function to check if a given column is valid. It will return:
# -1 if the column contains an invalid value
# 0 if the columncontains repeated values
# 1 is the column is valid.
def valid_col(col, grid):
  # Extracting the column.
  temp = [row[col] for row in grid]
  # Removing 0's.
  temp = list(filter(lambda a: a != 0, temp))
  # Checking for invalid values.
  if any(i < 0 and i > 9 for i in temp):
    #print("Invalid value")
    return -1
  # Checking for repeated values.
  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1
# Function to check if all the subsquares are valid. It will return:
# -1 if a subsquare contains an invalid value
# 0 if a subsquare contains repeated values
# 1 if the subsquares are valid.
def valid_subsquares(grid):
  for row in range(0, 9, 3):
      for col in range(0,9,3):
         temp = []
         for r in range(row,row+3):
            for c in range(col, col+3):
              if grid[r][c] != 0:
                temp.append(grid[r][c])
          # Checking for invalid values.
         if any(i < 0 and i > 9 for i in temp):
             #print("Invalid value")
             return -1
         # Checking for repeated values.
         elif len(temp) != len(set(temp)):
             return 0
  return 1
# Function to check if the board invalid.
def valid_board(grid):
  # Check each row and column.
  for i in range(9):
      res1 = valid_row(i, grid)
      res2 = valid_col(i, grid)
      # If a row or column is invalid then the board is invalid.
      if (res1 < 1 or res2 < 1):

          return False
  # If the rows and columns are valid then check the subsquares.
  res3 = valid_subsquares(grid)
  if (res3 < 1):
      return False
  else:
      return True