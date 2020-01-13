from pandas import read_csv

# Read the final csv output file
de = read_csv('output/3_style_edges.csv', usecols=['Cycle', 'Algorithm'])
dc = read_csv('output/3_style_corners.csv', usecols=['Cycle', 'Algorithm'])

# Initialize edges output content as an empty list of strings
edges_output = []

# Iterate through all unique cycles
for cycle in de['Cycle'].drop_duplicates():

  # Filter out the algorithms for this cycle
  algos = de[de['Cycle'] == cycle]['Algorithm']

  # Iterate through all filtered algorithms
  for i, algo in enumerate(algos):

    # Output content
    edges_output.append(' ' * 6 + f'<tr class="edges_All edges_{cycle[0]}">')

    # Cycle name needs to be mentioned only in the first row
    if i == 0:

      # Output content
      edges_output.append(' ' * 8 + f'<td rowspan="{len(algos)}">')
      edges_output.append(' ' * 10 + f'{cycle}')
      edges_output.append(' ' * 8 + '</td>')
    
    # Output content
    edges_output.append(' ' * 8 + '<td>')
    edges_output.append(' ' * 10 + f'{algo}')
    edges_output.append(' ' * 8 + '</td>')
    edges_output.append(' ' * 6 + '</tr>')

# Process output
print('Processing of edges done!')

# Initialize corners output content as an empty list of strings
corners_output = []

# Iterate through all unique cycles
for cycle in dc['Cycle'].drop_duplicates():

  # Filter out the algorithms for this cycle
  algos = dc[dc['Cycle'] == cycle]['Algorithm']

  # Iterate through all filtered algorithms
  for i, algo in enumerate(algos):

    # Output content
    corners_output.append(' ' * 6 + f'<tr class="corners_All corners_{cycle[0]}">')

    # Cycle name needs to be mentioned only in the first row
    if i == 0:

      # Output content
      corners_output.append(' ' * 8 + f'<td rowspan="{len(algos)}">')
      corners_output.append(' ' * 10 + f'{cycle}')
      corners_output.append(' ' * 8 + '</td>')
    
    # Output content
    corners_output.append(' ' * 8 + '<td>')
    corners_output.append(' ' * 10 + f'{algo}')
    corners_output.append(' ' * 8 + '</td>')
    corners_output.append(' ' * 6 + '</tr>')

# Process output
print('Processing of corners done!')

# Open the output HTML file
f = open('output/3_style.html', 'w')

# Read the template HTML and write additional data to output file
lines = open('html_template.html').readlines()
f.write('\n'.join(lines[:49] + edges_output + lines[50:86] + corners_output + lines[87:]))