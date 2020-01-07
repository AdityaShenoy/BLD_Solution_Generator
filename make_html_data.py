from pandas import read_csv

# Read the final csv files and convert them to HTML table format
read_csv('3_style_edges.csv').to_html('3_style_edges.html', index=False)
read_csv('3_style_corners.csv').to_html('3_style_corners.html', index=False)