from cube_brute_forcer import CubeBruteForcer as CBF
import pandas as pd

# Initialize object of CBF
cbf = CBF()

# Alias of moves of cbf
st = cbf.moves

# Initialize empty data
data = {'Cycle': [], 'Algorithm': [], 'Length': [], 'Type': []}

# Recording current number of moves being tested
cur_move_len = 0

# BH algorithms are maximum of length 13
while len(st) < 13:

  # Get the next move
  s = cbf.gen_nxt_move()

  # If the algorithm length has increased
  if cur_move_len < len(st):

    # Increment the current move length
    cur_move_len += 1

    # Print status on console
    print(f'Testing algorithms of length {cur_move_len}')

  # Check the cycles that are present on the cube
  cycles = cbf.cube.detect_cycle()

  # Corner cycles would be of length 9 each of length 3
  # Edge cycles would be of length 6 each of length 3
  # Avoiding center cycles
  if (len(cycles) in [6, 9]) and all([len(e) == 3 and e.isalpha() for e in cycles]):

    algo_type = 'Edge' if cycles[0].isupper() else 'Corner'

    # Iterate through all cycles
    for cycle in cycles:

      # Add appropriate rows
      data['Cycle'].append(cycle)
      data['Algorithm'].append(s)
      data['Length'].append(len(st))
      data['Type'].append(algo_type)

# Write the output to output.csv
pd.DataFrame(data).to_csv('output.csv', index=False)