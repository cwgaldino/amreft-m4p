# -*- coding: utf-8 -*-
"""
amreft-m4p example script 0.

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

import KUSB_488A_communication as gpib

# %% Initizalize communication
comm = initizalize()

# %% Send and receive identification (*idn?) message at adress 3
sent1 = gpib.send('*idn?', 3)
received1 = gpib.receive(3)
print(received1)

# %% Terminate communication
gpib.terminate(comm)
