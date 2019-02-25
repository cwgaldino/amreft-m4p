# -*- coding: utf-8 -*-
"""
Set of functions to control Nanovoltimeter Keithley2182A.

Python 3.7

@author: Carlos galdino
galdino@ifi.unicamp.br
"""


from KUSB_488A_communication import send_GPIB, receive_GPIB
from pathlib import Path

# %% Initial definitions

address_2182A = 3
bin_path = str(Path(r'..\bin'))

# %% Relevant commands
# I could have done separete functions for each of this commands, but they are
# used only once (or maybe twice) in the script so it is not worthy.

# I think it is easier to set the ACAL, FILTER, REL, and RATE by hand.

# Restore GPIB and remote options to default.
send_GPIB('*RST', address_2182A)

# Select function: ‘VOLTage’ or ‘TEMPerature’.
send_GPIB('\":sens:func \'volt\'\"', address_2182A)

# Select channel: 0 (internal temperature sensor), 1, or 2.
send_GPIB('\":sens:chan 1\"', address_2182A)

# Select channel 1 measure range; <n> = range.
# DCV1 function has five measurement ranges: 10mV, 100mV, 1V, 10V, and 100V
# DCV2 function has three measurement ranges: 100mV, 1V, and 10V
send_GPIB('\":sens:volt:chan1:rang 1\"', address_2182A)

# Enable/disable channel 1 auto range; (ON or OFF).
send_GPIB('\":sens:volt:chan1:rang:auto ON\"', address_2182A)

# %% Functions

def v():
    '''
    Reads a voltage value in Volts.

     address_2182A variables must be defined already. For example:
        address_2182A = 3
    '''

    send_GPIB(':READ?', address_2182A)

    return float(receive_GPIB(address_2182A))
