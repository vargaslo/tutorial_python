import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

from matplotlib import rc
plt.rc('text', usetex=True)

# Define function used for fitting data
def func(x, a, b, c):
  y = a * np.exp(-b * x) + c
  return y

# Generate noisy data
xdata = np.linspace(0, 4, 1000)
pinit = [2.5, 1.2, 0.5]
y = func(xdata, *pinit)
ydata = y + 0.2 * np.random.normal(size=len(xdata))

# Fit curve to noisy data
popt, pcov = opt.curve_fit(func, xdata, ydata)
fitted = func(xdata, *popt)

# Make a new figure and subplots
plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0))

# Plot data and fit in ax1
ax1.plot(xdata, ydata, '.', color='red', label='data')
line=r'$%s*\exp(-%s*x)+%s$' % (popt[0], popt[1], popt[2])
ax1.plot(xdata, fitted, color='blue', label=line)

# Plot residual in ax2
ax2.plot(xdata, (fitted-ydata), 'r', label='residual')

ax1.set_ylabel('Y Values ax1')
ax1.legend()

ax2.axhline(0, color='black')
ax2.set_xlabel('X Values')
ax2.set_ylabel('Y Values ax2')
ax2.legend()

plt.suptitle('Main title')
plt.show()
