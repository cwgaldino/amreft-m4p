# -*- coding: utf-8 -*-
"""
amreft-m4p example script 0.

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

# %% add amreft-m4p to the python PATH variable
import sys
from pathlib import Path
sys.path.append(str(Path(r'<PATH-to-amreft-m4p>\amreft-mp4')))

# %% import KUSB_488A_communication
import KUSB_488A_communication as gpib

# %% Initizalize communication
comm = gpib.initialize()

# %% Send and receive identification (*idn?) message at adress 3
sent = gpib.send('*idn?', 3)
received = gpib.receive(3)
print(received)

# %% Terminate communication
gpib.terminate(comm)
