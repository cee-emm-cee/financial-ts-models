import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-4, 4, 1000)

# Gaussian
gaussian = norm.pdf(x, 0, 1)

# Heston-like: mixture to capture fat tails + left skew
heston = 0.6 * norm.pdf(x, 0.05, 0.85) + 0.25 * norm.pdf(x, -0.15, 1.4) + 0.15 * norm.pdf(x, -0.5, 2.0)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, gaussian, 'b-', linewidth=2, label='Gaussian (Black-Scholes)')
ax.plot(x, heston, 'r-', linewidth=2, label='Heston (Stochastic Volatility)')
ax.fill_between(x, heston, where=(x < -2), alpha=0.3, color='red', label='Fat left tail')
ax.set_xlabel('Log Returns (standardized)', fontsize=12)
ax.set_ylabel('Density', fontsize=12)
ax.set_title('Return Distribution: Gaussian vs Heston', fontsize=14)
ax.legend(fontsize=11)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.55)
plt.tight_layout()
plt.savefig('heston_vs_gaussian.png', dpi=150)
plt.show()