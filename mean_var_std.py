import numpy as np

def calculate(list):
 
  #validate if list has less than 9 digits
  if len(list) < 9 or len(list) > 9:
    raise ValueError("List must contain nine numbers.")
  else:
  #convert list into 3x3 numpy array
    a = np.reshape(list, (3,3))
  #finds mean of axes, and flattened axis
  b = [(np.mean(a, axis=0)).tolist(), (np.mean(a, axis=1)).tolist(), np.mean(a)]
  #finds variance axes, and flattened axis
  c = [(np.var(a, axis=0)).tolist(), (np.var(a, axis=1)).tolist(), np.var(a)]
  #finds standard deviation axes, and flattened axis
  d = [(np.std(a, axis=0)).tolist(), (np.std(a, axis=1)).tolist(), np.std(a)]
  #finds max axes, and flattened axis
  e = [(np.max(a, axis=0)).tolist(), (np.max(a, axis=1)).tolist(), np.max(a)]
  #finds min axes, and flattened axis
  f = [(np.min(a, axis=0)).tolist(), (np.min(a, axis=1)).tolist(), np.min(a)]
  #finds sum axes, and flattened axis
  g = [(np.sum(a, axis=0)).tolist(), (np.sum(a, axis=1)).tolist(), (np.sum(a))]


  #create dictionary of lists, NOT Numpy arrays
  #dictionary would have all answers above.
  calculations = {
    'mean': b,
    'variance': c,
    'standard deviation': d,
    'max': e,
    'min': f,
    'sum': g,
  }
  return calculations
