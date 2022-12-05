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
from Agilent import Multimeter_34410A

# %% Initizalize communication
comm = gpib.initizalize()

# %% Initialize nanovoltimeter
address_34410A = 3
A34410A = Multimeter_34410A(address_34410A)

# %% get voltage
voltage = A34410A.v()
print(voltage)

# %% Terminate communication
gpib.terminate(comm)
