from pandas import read_csv
from algorithm import rotate

# This function removes any wide turn notations
# or cube rotations move from algorithm
def clean_algo(algo):
  
  # Replace all wide turn moves to their corresponding single slice move and whole cube rotation
  algo = algo.replace("r'", "L' x'")
  algo = algo.replace("r2", "L2 x2")
  algo = algo.replace("r", "L x")
  algo = algo.replace("l'", "R' x")
  algo = algo.replace("l2", "R2 x2")
  algo = algo.replace("l", "R x'")
  algo = algo.replace("u'", "D' y'")
  algo = algo.replace("u2", "D2 y2")
  algo = algo.replace("u", "D y")
  algo = algo.replace("d'", "U' y")
  algo = algo.replace("d2", "U2 y2")
  algo = algo.replace("d", "U y'")
  algo = algo.replace("f'", "B' z'")
  algo = algo.replace("f2", "B2 z2")
  algo = algo.replace("f", "B z")
  algo = algo.replace("b'", "F' z")
  algo = algo.replace("b2", "F2 z2")
  algo = algo.replace("b", "F z'")

  # Split moves on space
  algo = algo.split(' ')

  # Initialize empty list of strings for result
  res = []

  # Operation stack for rotation
  op = []

  # Iterate through all moves in the algorithm
  for i, e in enumerate(algo):

    # If the move is a rotation move
    if e[0] in 'xyz':

      # Push the operation on top of the stack
      op.append(e)

    # If the move is not a rotation move
    else:

      # Perform all operations on the stack
      for o in op[::-1]:

        # Rotate the move
        for _ in range({2: 1}.get(len(o), 3)):
          
          algo[i] = rotate(algo[i])[o[0]]
      
      # Append the move to the result
      res.append(algo[i])
  
  # Return cleaned algo
  return ' '.join(res)

# Read the raw parsed data
de = read_csv('output/parsed_edges.csv')
dc = read_csv('output/parsed_corners.csv')

# Apply cleaning algorithm to all the rows
de['Cleaned Algorithm'] = de['Algorithm'].apply(clean_algo)
dc['Cleaned Algorithm'] = dc['Algorithm'].apply(clean_algo)

# Save the new data
de.to_csv('output/cleaned_edges.csv', index=False)
dc.to_csv('output/cleaned_corners.csv', index=False)