from pandas import read_csv
from algorithm import rotate

# This function removes any wide turn notations
# or cube rotations move from algorithm
def clean_algo(algo):
  
  # Replace all wide turn moves to their corresponding 2 single slice moves
  algo = algo.replace("r'", "R' M")
  algo = algo.replace("r2", "R2 M2")
  algo = algo.replace("r", "R M'")
  algo = algo.replace("l'", "L' M'")
  algo = algo.replace("l2", "L2 M2")
  algo = algo.replace("l", "L M")
  algo = algo.replace("u'", "U' E")
  algo = algo.replace("u2", "U2 E2")
  algo = algo.replace("u", "U E'")
  algo = algo.replace("d'", "D' E'")
  algo = algo.replace("d2", "D2 E2")
  algo = algo.replace("d", "D E")
  algo = algo.replace("f'", "F' S'")
  algo = algo.replace("f2", "F2 S2")
  algo = algo.replace("f", "F S")
  algo = algo.replace("b'", "B' S")
  algo = algo.replace("b2", "B2 S2")
  algo = algo.replace("b", "B S'")

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