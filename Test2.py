import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Importation csv
data = pd.read_csv('winequality-white.csv', sep=";")

X = data.as_matrix(data.columns[:-1])

y = data.as_matrix([data.columns[-1]])

y = y.flatten()

# Création de la figure avec matplotlib aka plt
fig = plt.figure(figsize=(16, 12))

for feat_idx in range(X.shape[1]):

    ax = fig.add_subplot(3,4, (feat_idx+1))

    h = ax.hist(X[:, feat_idx], bins=50, color='steelblue',

                density=True, edgecolor='none')

    ax.set_title(data.columns[feat_idx], fontsize=14)
    plt.show()