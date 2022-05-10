import torch
import model
import numpy as np
a=np.ones((3,3))
b=np.zeros((3,3))
c=np.concatenate([a,b])
print(c.reshape((2,3,3)))