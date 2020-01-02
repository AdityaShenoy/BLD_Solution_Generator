from cube import Cube

# Class which will handle the brute force move generation
class CubeBruteForcer:

  # Constructor
  def __init__(self):

    # Initialize solved cube and empty list of moves
    self.cube = Cube()
    self.moves = []
    
    # Mapping from move letter to function
    self.letter_to_function = {'R': self.cube.R, 'U': self.cube.U, 'F': self.cube.F}

    # Mapping from current move to next move letter
    self.nxt_move = {'R': 'U', 'U': 'F'}
  
  # Returns next move in the brute force
  def gen_nxt_move(self):

    # Call the helper function -1 indicating the
    # index to increment which is the rightmost move
    self.gen_nxt_move_helper(-1)

    # Initialize empty list of strings of algorithms
    algo = []

    # Iterate through all moves
    for move in self.moves:

      # Append the move letter
      algo.append({
          "R11": "R", "R12": "R2", "R13": "R'",
          "R21": "M'", "R22": "M2", "R23": "M",
          "R31": "L'", "R32": "L2", "R33": "L",
          "U11": "U", "U12": "U2", "U13": "U'",
          "U21": "E'", "U22": "E2", "U23": "E",
          "U31": "D'", "U32": "D2", "U33": "D",
          "F11": "F", "F12": "F2", "F13": "F'",
          "F21": "S", "F22": "S2", "F23": "S'",
          "F31": "B'", "F32": "B2", "F33": "B",
        }[f'{move[0]}{move[1]}{move[2]}']
      )

    # Return the updated moves
    return ' '.join(algo)

  # Helper function which increments the move on the i index
  def gen_nxt_move_helper(self, i):

    # Aliases for the moves list, cube, and letter to function
    m, c, ltf = self.moves, self.cube, self.letter_to_function

    # If i overflows from the left
    if i == -len(m) - 1:

      # Insert R11 in the moves list at the left
      m.insert(0, ['R', 1, 1])
      
      # Perform R11 on the cube
      c.R(1, 1)
    
    # If the turn number is not equal to 3
    elif m[i][2] != 3:

      # Move the same slice one more time
      ltf[m[i][0]](m[i][1], 1)

      # Increment the turn number by 1
      m[i][2] += 1
    
    # Turn number is 3 but slice number is not equal to 3
    elif m[i][1] != 3:

      # Turn number is 3 so moving the same slice once more would nullify the move
      ltf[m[i][0]](m[i][1], 1)

      # Increment the last move slice by 1 and set turn number to 1
      m[i][1], m[i][2] = m[i][1] + 1, 1

      # Move the updated slice once
      ltf[m[i][0]](m[i][1], 1)
    
    # If the turn and slice numbers are 3 but move is not F
    elif m[i][0] != 'F':

      # Nullify the previous move
      ltf[m[i][0]](3, 1)

      # Set the move to next move and slice and turn numbers to 1 each
      m[i] = [self.nxt_move[m[i][0]], 1, 1]

      # Perform the updated move
      ltf[m[i][0]](1, 1)

      # While the move direction is same and previous slice number is greater or
      # equal to current slice indicating repeating parallel moves
      while i != -len(m) and m[i - 1][0] == m[i][0] and m[i - 1][1] >= m[i][1]:

        # Skip the current move and generate next move
        self.gen_nxt_move_helper(i)
    
    # Current move is F33
    else:

      # Nullify F33
      c.F(3, 1)

      # Recursively generate next move of the previous index
      self.gen_nxt_move_helper(i - 1)

      # Store R11 as the current move
      m[i] = ['R', 1, 1]

      # Perform R11
      c.R(1, 1)

      # While (current and previous move directions are same and
      # previous slice number is greater or equal to current slice number) or
      # current, previous and move before previous move directions are same
      while ((m[i - 1][0] == m[i][0]) and \
        (m[i - 1][1] >= m[i][1])) or\
        (i-2 != -len(m) - 1 and m[i-2][0] == m[i-1][0] == m[i][0]):

        # Skip the current move and generate next move
        self.gen_nxt_move_helper(i)