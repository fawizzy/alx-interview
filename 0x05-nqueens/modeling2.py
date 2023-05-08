
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# define the system
def sys(y, t):
    x1, x2, x3 = y
    dxdt = [x2, x3, -2 * x1 - 3 * x2 - x3 + 3]
    return dxdt

# initial conditions
x0 = [0, 0, 0]

# time range
t = np.linspace(0, 10, 1000)

# solve the ODE
x = odeint(sys, x0, t)

# plot the results
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Third Order System')
plt.legend(['x1', 'x2', 'x3'])
plt.show()