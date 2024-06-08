import numpy as np

depth = np.load("nerf_llff_fewshot_resize/fern/depths/00000.npy")
print(depth.shape)
print(depth.min(), depth.max())

import matplotlib.pyplot as plt
plt.imshow(depth)
plt.savefig("depth.png")