import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np


t = np.arange(-2, 2, 0.01)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)

fig.savefig("test.png")
plt.show()