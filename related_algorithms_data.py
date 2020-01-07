from pandas import read_csv, DataFrame
from related_algorithms import related_algo
from cube import Cube
from algorithm import apply
from os import system, name

# Read the cleaned algorithms from csv files
e_data = read_csv('cleaned_edges.csv')
c_data = read_csv('cleaned_corners.csv')

# Initialize related algo data as empty dictionary
e_rel_data = {'Cycle': [], 'Original': [], 'Cleaned': [], 'Transformation': [], 'Algorithm': []}
c_rel_data = {'Cycle': [], 'Original': [], 'Cleaned': [], 'Transformation': [], 'Algorithm': []}

# Initialize a cube
c = Cube()

# Store the length of the algorithm columns
le = len(e_data['Cleaned Algorithm'])
lc = len(c_data['Cleaned Algorithm'])

# Iterate through all algorithms in the data
for i, algo in enumerate(e_data['Cleaned Algorithm']):

  # Printing progress on console
  system({'nt': 'cls'}.get(name, 'clear'))
  print(f'{i+1} ({(i+1) / le * 100:.2f} %) edge algorithms processed out of {le}')

  # Find all related algorithms of algo
  rel_algos, ops = related_algo(algo)

  # Iterate through all related algos
  for rel_algo in rel_algos:
    
    # Solve the cube
    c.solve()

    # Apply the algorithm on the solved cube
    apply(c, rel_algo)

    # Detect cycles on the cube
    cycles = c.detect_cycle()

    # Iterate through all cycles
    for cycle in cycles:
      
      # Append the information to the data
      e_rel_data['Cycle'].append(cycle)
      e_rel_data['Original'].append(e_data['Algorithm'][i])
      e_rel_data['Cleaned'].append(algo)
      e_rel_data['Transformation'].append(ops[rel_algo])
      e_rel_data['Algorithm'].append(rel_algo)


# Iterate through all algorithms in the data
for i, algo in enumerate(c_data['Cleaned Algorithm']):

  # Printing progress on console
  system({'nt': 'cls'}.get(name, 'clear'))
  print(f'{le} (100.00 %) edge algorithms processed out of {le}')
  print(f'{i+1} ({(i+1) / lc * 100:.2f} %) corner algorithms processed out of {lc}')

  # Find all related algorithms of algo
  rel_algos, ops = related_algo(algo)

  # Iterate through all related algos
  for rel_algo in rel_algos:
    
    # Solve the cube
    c.solve()

    # Apply the algorithm on the solved cube
    apply(c, rel_algo)

    # Detect cycles on the cube
    cycles = c.detect_cycle()

    # Iterate through all cycles
    for cycle in cycles:
      
      # Append the information to the data
      c_rel_data['Cycle'].append(cycle.upper())
      c_rel_data['Original'].append(e_data['Algorithm'][i])
      c_rel_data['Cleaned'].append(algo)
      c_rel_data['Transformation'].append(ops[rel_algo])
      c_rel_data['Algorithm'].append(rel_algo)


# Create a data frame of the data generated
e_new_data = DataFrame(e_rel_data)
c_new_data = DataFrame(c_rel_data)

# Sort the data by cycles
e_new_data.sort_values(by='Cycle', inplace=True)
c_new_data.sort_values(by='Cycle', inplace=True)

# Store all data to debugging csv files
e_new_data.to_csv('debugging_edges.csv', index=False)
c_new_data.to_csv('debugging_corners.csv', index=False)

# Store only cycle and algorithm columns to the final csv file
e_new_data[['Cycle', 'Algorithm']].to_csv('3_style_edges.csv', index=False)
c_new_data[['Cycle', 'Algorithm']].to_csv('3_style_corners.csv', index=False)