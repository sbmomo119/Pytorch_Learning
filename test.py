import torch
import numpy as np

a = np.array([2,3.3])
print(torch.from_numpy(a))

print(torch.FloatTensor([2,3.2]))

a=np.ones([2,3])

print(torch.from_numpy(a))



