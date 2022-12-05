# -*- coding: utf-8 -*-
"""
Set of functions to control Lakeshore 340 temperature controller.

Python 3.7

@author: Carlos galdino
galdino@ifi.unicamp.br
"""
# %% add amreft-m4p to the python PATH variable
import sys
from pathlib import Path
sys.path.append(str(Path(r'C:\Users\carlo\github\amreft-m4p\amreft-mp4')))

# %% import KUSB_488A_communication
import KUSB_488A_communication as gpib
from Lakeshore import Lakeshore_340

# %% Initizalize communication
comm = gpib.initizalize()

# %% Initialize lakeshore 340
address_340 = 1
L340 = Lakeshore_340(address_340)

# %% set/get temperature
L340.t(300)  # set setpoint to 300 K
L340.t()     # get temperature
temperature = L340.t()  # get temperature and save in a variable

L340.heater_output()  # get heater output

L340.heater_range(0)  # Turn heater off
L340.heater_range()   # get heater range

# %% Terminate communication
gpib.terminate(comm)
