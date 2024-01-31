import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  
  list1 = np.array(list)
  list_array = list1.reshape(3,3)

  calculations = {}
  
  calculations['mean'] = [list_array.mean(axis=0).tolist(), list_array.mean(axis=1).tolist(), list_array.mean()]
  calculations['variance'] = [list_array.var(axis=0).tolist(), list_array.var(axis=1).tolist(), list_array.var()]
  calculations['standard deviation'] = [list_array.std(axis=0).tolist(), list_array.std(axis=1).tolist(), list_array.std()]
  calculations['max'] = [list_array.max(axis=0).tolist(), list_array.max(axis=1).tolist(), list_array.max()]
  calculations['min'] = [list_array.min(axis=0).tolist(), list_array.min(axis=1).tolist(), list_array.min()]
  calculations['sum'] = [list_array.sum(axis=0).tolist(), list_array.sum(axis=1).tolist(), list_array.sum()]

  return calculations