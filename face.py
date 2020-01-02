# Face represents the 6 faces of the Rubik's cube
class Face:


  # Constructor
  def __init__(self, color):

    # Initialize the stickers of the face by
    # the color passed to the constructor
    # Lower case letters represent corners
    # Upper case letters represent edges
    # Numbers represent the centers in the order of Speff's lettering scheme
    self.stickers = {
      'W': ['a', 'A', 'b',
            'D', '1', 'B',
            'd', 'C', 'c'],
      'O': ['e', 'E', 'f',
            'H', '2', 'F',
            'h', 'G', 'g'],
      'G': ['i', 'I', 'j',
            'L', '3', 'J',
            'l', 'K', 'k'],
      'R': ['m', 'M', 'n',
            'P', '4', 'N',
            'p', 'O', 'o'],
      'B': ['q', 'Q', 'r',
            'T', '5', 'R',
            't', 'S', 's'],
      'Y': ['u', 'U', 'v',
            'X', '6', 'V',
            'x', 'W', 'w']
    }[color]

    # This is the correct position of the face
    self.correct_pos = self.stickers[:]
  

  # Rotate the stickers clockwise
  def clock_wise(self):

    # Alias for stickers
    a = self.stickers

    # cycles = (0,2,8,6), (1,5,7,3)
    a[2], a[8], a[6], a[0] = a[0], a[2], a[8], a[6]
    a[5], a[7], a[3], a[1] = a[1], a[5], a[7], a[3]
  

  # Rotate the stickers anticlockwise
  def anti_clock_wise(self):

    # Alias for stickers
    a = self.stickers

    # cycles = (6,8,2,0), (3,7,5,1)
    a[0], a[2], a[8], a[6] = a[2], a[8], a[6], a[0]
    a[1], a[5], a[7], a[3] = a[5], a[7], a[3], a[1]