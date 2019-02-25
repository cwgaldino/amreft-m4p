# -*- coding: utf-8 -*-
"""
amreft-m4p example script 0.

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

from KUSB_488A_communication import init_gpib, terminate_gpib, send_GPIB, receive_GPIB

# %% Initizalize communication

comm_gpib = init_gpib()

# %% Send and receive identification message on adress 3

sent1 = send_GPIB('*idn?', 3)
received1 = receive_GPIB(3)
print(received1)

# %% Terminate communication

terminate_gpib(comm_gpib)
