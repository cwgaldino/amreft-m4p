# -*- coding: utf-8 -*-
"""
amreft-m4p example script 0.

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

from KUSB_488A_communication import init_gpib, send_GPIB, receive_GPIB
import threading
import sys

#sys.path.append(str(Path('../bin")))

# %% Initizalize communication

init_thread = threading.Thread(target=init_gpib)
init_thread.start()

# Ask about threads if necessary
#threading.active_count()
#init_thread.isAlive()


# %% Send and receive identification message on adress 3

sent1 = send_GPIB('*idn?', 3)
received1 = receive_GPIB(3)

print(received1)
