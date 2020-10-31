from copy import deepcopy as copy

# Converts computer understandable algorithm with 
# notations of direction, slice and turn
# to human readable notations
def to_human_readable(algo):
  
  # Mapping from direction, slice, turn notation to human readable notation
  d = {
    "R11": "R" , "R12": "R2", "R13": "R'",
    "R21": "M'", "R22": "M2", "R23": "M" ,
    "R31": "L'", "R32": "L2", "R33": "L" ,
    "U11": "U" , "U12": "U2", "U13": "U'",
    "U21": "E'", "U22": "E2", "U23": "E" ,
    "U31": "D'", "U32": "D2", "U33": "D" ,
    "F11": "F" , "F12": "F2", "F13": "F'",
    "F21": "S" , "F22": "S2", "F23": "S'",
    "F31": "B'", "F32": "B2", "F33": "B" ,
  }
  
  # Initialize empty list of strings
  result = []

  # Iterate through all moves in the algo
  for move in algo:

    # Append the converted move into the result list
    result.append(d[f'{move[0]}{move[1]}{move[2]}'])
  
  # Return algorithm by space separating it
  return ' '.join(result)


# Converts human understandable algorithm with 
# to computer readable algorithms having
# notations of direction, slice and turn
def to_computer_readable(algo):
  
  # Mapping from human readable notation to direction, slice, turn notation
  d = {
    "R" : "R11", "R2": "R12", "R'": "R13",
    "M'": "R21", "M2": "R22", "M" : "R23",
    "L'": "R31", "L2": "R32", "L" : "R33",
    "U" : "U11", "U2": "U12", "U'": "U13",
    "E'": "U21", "E2": "U22", "E" : "U23",
    "D'": "U31", "D2": "U32", "D" : "U33",
    "F" : "F11", "F2": "F12", "F'": "F13",
    "S" : "F21", "S2": "F22", "S'": "F23",
    "B'": "F31", "B2": "F32", "B" : "F33",
  }

  # Initialize empty list of strings
  result = []

  # Iterate through all moves in the algo
  for move in algo.split(' '):

    # Append the converted move into the result list
    temp = d[move]
    result.append([temp[0], int(temp[1]), int(temp[2])])
  
  # Return the resulting list
  return result


# Returns inverse of the algorithm
def invert(algo):
  
  # If human readable algorithm is passed, convert to computer readable
  algo1 = to_computer_readable(algo) if type(algo) is str else copy(algo)

  # Read the moves in reverse and flip the turn number
  result =  [[e[0], e[1], {1: 3, 2: 2, 3: 1}[e[2]]] for e in algo1[::-1]]

  # Return the result in the type which was passed in the parameter
  return result if type(algo) is list else to_human_readable(result)


# Returns mirror of the algorithm wrt RL, UD and FB planes
def mirror(algo):
  
  # If the algorithm is passed in human readable form
  # convert it to computer readable
  algo1 = copy(algo) if type(algo) is list else to_computer_readable(algo)

  # Make 3 copies of algo1
  rl_result, ud_result, fb_result = copy(algo1), copy(algo1), copy(algo1)

  # This is a mapping to reverse slice and turn numbers
  rev = {1: 3, 2: 2, 3: 1}

  # Iterate through all moves in algo1
  for i, e in enumerate(algo1):

    # If the direction is R
    if e[0] == 'R':

      # Mirror slice number
      rl_result[i][1] = rev[e[1]]

      # Invert turn numbers of other notations
      ud_result[i][2] = rev[e[2]]
      fb_result[i][2] = rev[e[2]]
    
    # If the direction is U
    elif e[0] == 'U':

      # Mirror slice number
      ud_result[i][1] = rev[e[1]]

      # Invert turn numbers of other notations
      rl_result[i][2] = rev[e[2]]
      fb_result[i][2] = rev[e[2]]

    # If the direction is F
    else:

      # Mirror slice number
      fb_result[i][1] = rev[e[1]]

      # Invert turn numbers of other notations
      rl_result[i][2] = rev[e[2]]
      ud_result[i][2] = rev[e[2]]
  
  # Store the 3 results in a dictionary
  result = {'RL': rl_result, 'UD': ud_result, 'FB': fb_result}

  # If the input type was list return the result as it is
  # else convert each result into human readable format
  return result if type(algo) is list else \
    {k: to_human_readable(v) for k, v in result.items()}


# Returns rotated version of the algorithms on 3 axis i.e. x, y, and z
def rotate(algo):
  
  # If the algorithm passed is in human readable formart
  # convert it to computer readable form
  algo1 = copy(algo) if type(algo) is list else to_computer_readable(algo)

  # Make 3 copies of algo1
  x_result, y_result, z_result = copy(algo1), copy(algo1), copy(algo1)

  # This is a mapping to invert slice and turn numbers
  rev = {1: 3, 2: 2, 3: 1}

  # Iterate through all moves in the algo
  for i, e in enumerate(algo1):

    # If direction is R
    if e[0] == 'R':

      # Rotation results in y and z rotations
      y_result[i][0] = 'F'
      z_result[i] = ['U', rev[e[1]], rev[e[2]]]
    
    # If direction is U
    elif e[0] == 'U':

      # Rotation results in x and z rotations
      x_result[i] = ['F', rev[e[1]], rev[e[2]]]
      z_result[i][0] = 'R'
    
    # If direction is F
    else:

      # Rotation results in x and y rotations
      x_result[i][0] = 'U'
      y_result[i] = ['R', rev[e[1]], rev[e[2]]]
  
  # Store the 3 results in a dictionary
  result = {'x': x_result, 'y': y_result, 'z': z_result}

  # If the input type was list return the result as it is
  # else convert each result into human readable format
  return result if type(algo) is list else \
    {k: to_human_readable(v) for k, v in result.items()}


# Performs the algorithm on the cube
def apply(cube, algo):

  # If the input algorithm in human readable form convert it to computer readable form
  algo1 = copy(algo) if type(algo) is list else to_computer_readable(algo)

  # Mapping from move to function
  d = {'R': cube.R, 'U': cube.U, 'F': cube.F}

  # Iterate through all moves in the algo
  for move in algo1:

    # Apply move on the cube
    d[move[0]](int(move[1]), int(move[2]))
  
  # Return the cube after applying the algorithm on it
  return cube
