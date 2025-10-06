import numpy as np

def normalize_vector(x):
  return (x - np.nanmean(x)) / np.nanstd(x)