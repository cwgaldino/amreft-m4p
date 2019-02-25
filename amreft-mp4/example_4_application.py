# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:13:08 2019

@author: Carlos
"""

import time
import matplotlib.pyplot as plt
import numpy as np
import threading  # Enable threading of processes
from galdinoFunctions_gpib_V1.py import *

# %% Functions

def update_line(hl, ax, new_dataX, new_dataY):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_dataX))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_dataY))
    ax.relim()
    ax.autoscale_view()
    plt.draw()



# %% Initizalize communication

init_thread = threading.Thread(target=init_gpib)
init_thread.start()

# %%
# Parameters
t_err = 1 # Temperature accepted error (K)
a = []
sigma = np.array(a)
sigma.append(1)

# start plot: temperature vs time
fig_temp, ax_temp = plt.subplots()
line_temp, = ax_temp.plot([], [])


setpoint=310
t(setpoint)
time.sleep(5*60)  # 5 min

# Plot temperature during 30s (1s per point)
sec = 0
while(sec < 30):
    update_line(line_temp, ax_temp, sec, t())
    time.sleep(1)
    sec += 1

# Measure conductivity
a(10e-3)
v()
t()

# tempereature check
if t()>setpoint-t_err or t()<setpoint+t_err:
    time.sleep(1*60)  # 1 min










# %%


