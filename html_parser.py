from requests import get
from pandas import DataFrame
from html.parser import HTMLParser
from re import sub
from related_algorithms import related_algo

# Overrided HTML Parser class
class MyHTMLParser(HTMLParser):


  # Overrided constructor
  def __init__(self):
    super().__init__(convert_charrefs=True)
    
    # Variables to track row number and column number to avoid header row and Cycle and Name column
    self.row_num, self.col_num = -1, -1
    
    # Flag that tracks whether the parser is inside td tag or not
    self.data_flag = False
    
    # Initialize algorithm data to an empty data dictionary
    self.a_data = {}


  # Overrided function for handling start tag
  def handle_starttag(self, tag, attrs):

    # When table tag is encountered
    if tag == 'table':

      # Reset data, row num, and col num
      self.col_num = -1
      self.row_num = -1
      self.a_data = {'Algorithm': []}
    
    # If td tag is encountered
    elif tag == 'td':

      # Set data flag to True
      self.data_flag = True

      # Incremenent col num by 1
      self.col_num += 1
    
    # If tr tag is encountered
    elif tag == 'tr':

      # Increment row number
      self.row_num += 1

      # Reset col number
      self.col_num = -1


  # Overrided function for handling end tag
  def handle_endtag(self, tag):

    # If td end tag is encountered
    if tag == 'td':
      
      # Set data flag to False
      self.data_flag = False


  # Overrided function for handling data
  def handle_data(self, data):

    # If the data encountered is present inside the td tags, not in header row and is in second column
    if self.data_flag and self.row_num > 0 and self.col_num == 1:

      # If the data does not contain algorithm length and ** notation
      if data.find('(') == data.find('*') == -1:

        # Remove unwanted whitespaces from the algorithm and append it to data
        self.a_data['Algorithm'].append(sub(' *\n *', ' ', data.strip()))


# Get the contents of the files
edge_content = open('edges.txt').read()
corner_content = open('corners.txt').read()

# Initialize the parser object
mhp = MyHTMLParser()

# Feed the edge content to the parser
mhp.feed(edge_content)

# Store the can_data to a csv file
d = DataFrame(mhp.a_data)
d.to_csv('parsed_edges.csv', index=False)

# Feed the corner content to the parser
mhp.feed(corner_content)

# Store the can_data to a csv file
d = DataFrame(mhp.a_data)
d.to_csv('parsed_corners.csv', index=False)