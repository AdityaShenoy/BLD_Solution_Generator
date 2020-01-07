from algorithm import *


# Finds all related algorithms with the help of a helper function
def related_algo(algo):

  # Call helper function with first parameter as a set containing algo
  # second parameter as algorithm, third parameter as a mapping to what
  # transformations were applied to the original algorithm
  return related_algo_helper({algo}, algo, {algo: ''})


# This is a helper function which takes 3 parameters
# First parameter is the visited set to avoid working on same algo more than once
# Second parameter is the last visited algorithm
# Third parameter is a mapping from algo to string of transformations that are applied to the algo
def related_algo_helper(vis, algo, ops):

  # Invert, mirror and rotate the algo
  imr_res = imr(algo)

  # Iterate through all newly obtained algos
  for a, op in [(imr_res[t], t) for t in 'irufxyz']:
    
    # If the algo is not visited
    if a not in vis:

      # Add the algo to visited set
      vis.add(a)

      # Add the current operation to the input algorithm transformation string
      ops[a] = ops[algo] + op

      # Call this function recursively
      vis, ops = related_algo_helper(vis, a, ops)
  
  # Return the set with all related algos
  return vis, ops


# imr stands for invert, mirror and rotate
# This function returns the above transformations
# of the algo passed in the parameter
def imr(algo):

  # Calculate transformations
  algo_i = invert(algo)
  algo_m = mirror(algo)
  algo_r = rotate(algo)

  # Result will be a dictionary having all the transformations
  return {
    'i': algo_i,
    'r': algo_m['RL'],
    'u': algo_m['UD'],
    'f': algo_m['FB'],
    'x': algo_r['x'],
    'y': algo_r['y'],
    'z': algo_r['z']
  }

