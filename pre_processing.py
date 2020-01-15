from pandas import read_csv
from algorithm import rotate

# This function removes any wide turn notations
# or cube rotations move from algorithm
def clean_algo(algo):
  
  # Split the algo into its moves separated by space
  algo_split = algo.split(' ')

  # This mapping is to replace wide turn moves into their corresponding 2 slice moves
  wide_to_2_slice = {
    "r'": "R' M",
    "r2": "R2 M2",
    "r" : "R M'",
    "l'": "L' M'",
    "l2": "L2 M2",
    "l" : "L M",
    "u'": "U' E",
    "u2": "U2 E2",
    "u" : "U E'",
    "d'": "D' E'",
    "d2": "D2 E2",
    "d" : "D E",
    "f'": "F' S'",
    "f2": "F2 S2",
    "f" : "F S",
    "b'": "B' S",
    "b2": "B2 S2",
    "b" : "B S'",
  }

  # If the first or last move is a wide turn move, then replace it with above mapping
  algo_split[0] = wide_to_2_slice.get(algo_split[0], algo_split[0])
  algo_split[-1] = wide_to_2_slice.get(algo_split[-1], algo_split[-1])

  # This mapping is to replace wide turn moves into their corresponding single slice move and rotation
  wide_to_slice_rotate = {
    "r'": "L' x'",
    "r2": "L2 x2",
    "r" : "L x",
    "l'": "R' x",
    "l2": "R2 x2",
    "l" : "R x'",
    "u'": "D' y'",
    "u2": "D2 y2",
    "u" : "D y",
    "d'": "U' y",
    "d2": "U2 y2",
    "d" : "U y'",
    "f'": "B' z'",
    "f2": "B2 z2",
    "f" : "B z",
    "b'": "F' z",
    "b2": "F2 z2",
    "b" : "F z'",
  }

  # Replace all wide turn moves to their corresponding single slice move and whole cube rotation
  algo_split = list(map(lambda x: wide_to_slice_rotate.get(x, x), algo_split))

  # Join and split moves on space
  algo_split = ' '.join(algo_split).split(' ')

  # Initialize empty list of strings for result
  res = []

  # Operation stack for rotation
  op = []

  # Iterate through all moves in the algorithm
  for i, e in enumerate(algo_split):

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
          
          algo_split[i] = rotate(algo_split[i])[o[0]]
      
      # Append the move to the result
      res.append(algo_split[i])
  
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