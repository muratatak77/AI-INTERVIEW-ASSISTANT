# test_numpy.py
import torch
import numpy as np

arr = np.array([1.0, 2.0, 3.0])
t = torch.from_numpy(arr)
print(t)
