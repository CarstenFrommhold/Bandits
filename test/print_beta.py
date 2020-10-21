from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(1, 1)

a = 255
b = 578

x = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 100)
ax.plot(x, beta.pdf(x, a, b),
       'r-', lw=5, alpha=0.6, label='beta pdf')
plt.show()