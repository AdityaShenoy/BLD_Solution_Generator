from pandas import read_csv

# Given a string of algorithm, calculate its score
def score(s):

  # Weights of difficulty assigned to RMLUEDFSB
  wt = {
    'R': 0,
    'L': 0,
    'M': 0,
    'U': 0,
    'E': 0,
    'D': 0,
    'F': 1,
    'S': 1,
    'B': 2,
  }

  # Check count the move in the algo and multiply the weight to it
  return sum([wt[e] * s.count(e) for e in 'RMLUEDFSB'])

# Read files
de = read_csv('output/all_edges.csv')
dc = read_csv('output/all_corners.csv')

# Assign score to each algorithm
de['Score'] = de['Algorithm'].apply(score)
dc['Score'] = dc['Algorithm'].apply(score)

# Sort the data by cycle and if they are same then by score
de.sort_values(by=['Cycle','Score'], inplace=True)
dc.sort_values(by=['Cycle','Score'], inplace=True)

# Save the sorted data to new csv output files
de.to_csv('output/3_style_edges.csv', index=False)
dc.to_csv('output/3_style_corners.csv', index=False)