from face import Face

# Cube represents the Rubik's cube
class Cube:


  # Constructor
  def __init__(self):

    # Initialize 6 faces of the cube
    self.up = Face('W')
    self.front = Face('G')
    self.right = Face('R')
    self.back = Face('B')
    self.left = Face('O')
    self.down = Face('Y')
  

  # Turn the nth slice from right clockwise t times
  def R(self, n, t):

    # Debugging print
    # print(f'R{n}{t}', end=' ')

    # Aliases for the faces of the cube
    u, f, r, b, l, d = self.up.stickers, self.front.stickers, \
                       self.right.stickers, self.back.stickers, \
                       self.left.stickers, self.down.stickers

    # Repeat t times
    for _ in range(t):

      # If rightmost slice is being turned
      if n == 1:
        self.right.clock_wise()
      
      # If leftmost slice is being turned
      if n == 3:
        self.left.anti_clock_wise()
      
      # Cycles (u, b, d, f)
      u[3-n::3], b[5+n::-3], d[3-n::3], f[3-n::3] = f[3-n::3], \
                             u[3-n::3], b[5+n::-3], d[3-n::3]
      
    # Return the updated cube
    return self
  

  # Turn the nth slice from top t times
  def U(self, n, t):

    # Debugging print
    # print(f'U{n}{t}', end=' ')

    # Aliases for the faces of the cube
    u, f, r, b, l, d = self.up.stickers, self.front.stickers, \
                       self.right.stickers, self.back.stickers, \
                       self.left.stickers, self.down.stickers

    # Repeat t times
    for _ in range(t):

      # If upmost slice is being turned
      if n == 1:
        self.up.clock_wise()
      
      # If downmost slice is being turned
      if n == 3:
        self.down.anti_clock_wise()
      
      # Cycles (f, l, b, r)
      f[3*n-3:3*n], l[3*n-3:3*n], b[3*n-3:3*n], r[3*n-3:3*n] = r[3*n-3:3*n], \
                                   f[3*n-3:3*n], l[3*n-3:3*n], b[3*n-3:3*n]

    # Return the updated cube
    return self


  # Turn the nth slice from front t times
  def F(self, n, t):

    # Debugging print
    # print(f'F{n}{t}', end=' ')

    # Aliases for the faces of the cube
    u, f, r, b, l, d = self.up.stickers, self.front.stickers, \
                       self.right.stickers, self.back.stickers, \
                       self.left.stickers, self.down.stickers

    # Repeat t times
    for _ in range(t):

      # If frontmost slice is being turned
      if n == 1:
        self.front.clock_wise()
      
      # If backmost slice is being turned
      if n == 3:
        self.back.anti_clock_wise()
      
      # Cycles (u, r, d, l)
      u[9-3*n:12-3*n], r[n-1::3], d[3*n-3:3*n], l[3-n::3] = l[3-n::3][::-1], \
                                 u[9-3*n:12-3*n], r[n-1::3][::-1], d[3*n-3:3*n]

    # Return the updated cube
    return self


  # Printing cube sticker state
  def __str__(self):

    # Aliases for the faces of the cube
    u, f, r, b, l, d = self.up.stickers, self.front.stickers, \
                       self.right.stickers, self.back.stickers, \
                       self.left.stickers, self.down.stickers

    return \
      ' '  + ' '  + ' '  + u[0] + u[1] + u[2] + '\n' + \
      ' '  + ' '  + ' '  + u[3] + u[4] + u[5] + '\n' + \
      ' '  + ' '  + ' '  + u[6] + u[7] + u[8] + '\n' + \
      l[0] + l[1] + l[2] + f[0] + f[1] + f[2] + r[0] + r[1] + r[2] + '\n' + \
      l[3] + l[4] + l[5] + f[3] + f[4] + f[5] + r[3] + r[4] + r[5] + '\n' + \
      l[6] + l[7] + l[8] + f[6] + f[7] + f[8] + r[6] + r[7] + r[8] + '\n' + \
      ' '  + ' '  + ' '  + d[0] + d[1] + d[2] + '\n' + \
      ' '  + ' '  + ' '  + d[3] + d[4] + d[5] + '\n' + \
      ' '  + ' '  + ' '  + d[6] + d[7] + d[8] + '\n' + \
      ' '  + ' '  + ' '  + b[8] + b[7] + b[6] + '\n' + \
      ' '  + ' '  + ' '  + b[5] + b[4] + b[3] + '\n' + \
      ' '  + ' '  + ' '  + b[2] + b[1] + b[0]
  

  # Detects cycles after performing the algorithm
  def detect_cycle(self):

    # Initialize mapping of moves
    moves = dict()

    # Iterate through all the faces of the cube
    for face in [self.up, self.front, self.left, self.right, self.down, self.back]:

      # Iterate through all stickers of the face
      for i in range(9):

        # If the current sticker does not match original sticker of that position
        if face.stickers[i] != face.correct_pos[i]:

          # moves[A] = B means A piece has gone to position B
          moves[face.stickers[i]] = face.correct_pos[i]
    
    # Initalize cycle list
    cycles = []

    # Iterate through all the mappings of the moves
    for m in list(moves):

      # The moves can be deleted in the loop
      # So check its presence
      if m in moves:

        # Initialize empty string of cycle
        s = ''

        # Iterate until we reach the same sticker back which will be deleted
        while m in moves:

          # Append the cycle letter
          s += m

          # Move to the next letter of the cycle
          m = moves[m]

          # Delete the previous cycle for avoiding infinite loop
          del moves[s[-1]]
        
        # Append all permutations of cycles to the list
        for i in range(len(s)):
          cycles.append(s[i:] + s[:i])

    # Return the cycles
    return cycles
  

  # Solves the cube
  def solve(self):

    # Following lines updates the stickers of all the cubes
    # to its correct position thus solve them
    self.up.stickers = self.up.correct_pos[:]
    self.down.stickers = self.down.correct_pos[:]
    self.front.stickers = self.front.correct_pos[:]
    self.back.stickers = self.back.correct_pos[:]
    self.left.stickers = self.left.correct_pos[:]
    self.right.stickers = self.right.correct_pos[:]