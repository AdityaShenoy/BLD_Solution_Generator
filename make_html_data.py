from pandas import read_csv

# Read the final csv output file
de = read_csv('output/3_style_edges.csv', usecols=['Cycle', 'Algorithm'])
dc = read_csv('output/3_style_corners.csv', usecols=['Cycle', 'Algorithm'])

# Initialize output contents of the HTML content apart from the actual table data
output = ['<!doctype html>\n<html>\n<head>\n  <!-- Latest compiled and minified CSS -->\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">\n\n  <!-- jQuery library -->\n  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>\n\n  <!-- Latest compiled JavaScript -->\n  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>\n\n  <title>3 Style Algorithms</title>\n</head>\n<body>\n  <div id="edges_container" class="col-lg-6">\n    <label for="edges_select">Select Edge Buffer: </label>\n    <select id="edges_select" class="form-control" onchange="filterEdges(this.value)">\n      <option value="All">All</option>\n      <option value="A">A</option>\n      <option value="B">B</option>\n      <option value="C">C</option>\n      <option value="D">D</option>\n      <option value="E">E</option>\n      <option value="F">F</option>\n      <option value="G">G</option>\n      <option value="H">H</option>\n      <option value="I">I</option>\n      <option value="J">J</option>\n      <option value="K">K</option>\n      <option value="L">L</option>\n      <option value="M">M</option>\n      <option value="N">N</option>\n      <option value="O">O</option>\n      <option value="P">P</option>\n      <option value="Q">Q</option>\n      <option value="R">R</option>\n      <option value="S">S</option>\n      <option value="T">T</option>\n      <option value="U">U</option>\n      <option value="V">V</option>\n      <option value="W">W</option>\n      <option value="X">X</option>\n    </select>\n    <table id="edges_table" class="table table-bordered">\n      <tr class="edges_header">\n        <th>Cycle</th>\n        <th>Algorithm</th>\n      </tr>', '    </table>\n  </div>\n  <div id="corners_container" class="col-lg-6">\n    <label for="corners_select">Select Corner Buffer: </label>\n    <select id="corners_select" class="form-control" onchange="filterCorners(this.value)">\n      <option value="All">All</option>\n      <option value="A">A</option>\n      <option value="B">B</option>\n      <option value="C">C</option>\n      <option value="D">D</option>\n      <option value="E">E</option>\n      <option value="F">F</option>\n      <option value="G">G</option>\n      <option value="H">H</option>\n      <option value="I">I</option>\n      <option value="J">J</option>\n      <option value="K">K</option>\n      <option value="L">L</option>\n      <option value="M">M</option>\n      <option value="N">N</option>\n      <option value="O">O</option>\n      <option value="P">P</option>\n      <option value="Q">Q</option>\n      <option value="R">R</option>\n      <option value="S">S</option>\n      <option value="T">T</option>\n      <option value="U">U</option>\n      <option value="V">V</option>\n      <option value="W">W</option>\n      <option value="X">X</option>\n    </select>\n    <table id="corners_table" class="table table-bordered">\n      <tr class="corners_header">\n        <th>Cycle</th>\n        <th>Algorithm</th>\n      </tr>', "    </table>\n  </div>\n  <script>\n\n    $('table tr').hide();\n\n    function filterEdges(val) {\n      $('#edges_table tr').hide();\n      $('.edges_'+val).show();\n      $('.edges_header').show();\n    }\n\n    function filterCorners(val) {\n      $('#corners_table tr').hide();\n      $('.corners_'+val).show();\n      $('.corners_header').show();\n    }\n\n  </script>\n</body>\n</html>"]

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

# Open the output HTML file
f = open('output/3_style.html', 'w')

# Write the ouput
f.write('\n'.join([output[0], '\n'.join(edges_output), output[1], '\n'.join(corners_output), output[2]]))