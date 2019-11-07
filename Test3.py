import pandas as pd


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# Définition de la VUE nombres de points
x = np.linspace(-2, 2, 2000)

# Get current size
fig_size = plt.rcParams["figure.figsize"]

# Taille de la figure
fig_size[0] = 8
fig_size[1] = 6
plt.rcParams["figure.figsize"] = fig_size

#Taille du graph
axes = plt.gca()

axes.set_xlim([-2,2])
axes.set_ylim([-2,2])


plt.plot(x, x, label='X = X')
plt.plot(x, x**2, label='X^2',color='black', marker='x', linestyle='dashed',
        linewidth=1, markersize=2)
plt.plot(x, x**3, label='X^3',color='yellow')

plt.grid()

plt.xlabel('Axe X ')
plt.ylabel('Axe Y')
plt.title("Graph X / Y")
plt.legend()

plt.show()