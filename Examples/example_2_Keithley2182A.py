# -*- coding: utf-8 -*-
"""
Set of functions to control Nanovoltimeter Keithley2182A.

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
from Keithley import Nanovoltimeter_2182A

# %% Initizalize communication
comm = gpib.initizalize()

# %% Initialize nanovoltimeter
address_2182A = 3
K2182A = Nanovoltimeter_2182A(address_2182A)

# %% get voltage
voltage = K2182A.v()
print(voltage)

# %% Terminate communication
gpib.terminate(comm)
