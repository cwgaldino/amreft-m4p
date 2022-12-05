# -*- coding: utf-8 -*-
"""
Set of functions to control Current Source Keithley 6221.

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
from Keithley import CurrentSource_6221

# %% Initizalize communication
comm = gpib.initialize()

# %% Initialize current source
address_6221 = 3
K6221 = CurrentSource_6221(address_6221)

# %% Set current
K6221.set_range(12e-3)  # Selects the 20mA range
K6221.set_A(12e-3)  # Sets the DC output to 12mA
K6221.set_compliance(10)  # Sets voltage compliance to 10V

# %% Terminate communication
gpib.terminate(comm)
