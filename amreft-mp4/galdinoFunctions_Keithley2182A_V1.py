# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:52:09 2019

@author: Carlos galdino
galdino@ifi.unicamp.br
"""


from galdinoFunctions_gpib_V1.py import *

# %% Initial definitions

address_2182A = 3
bin_path = r'D:\amreft-m4p\amreft-m4p_V1_galdino\bin'

# %% Relevant commands
# I could have done separete functions for each of this commands, but they are
# used only once (or maybe twice) in the script so it is not worthy.

# I think it is easier to set the ACAL, FILTER, REL, and RATE by hand.

# Restore GPIB and remote options to default.
send_GPIB('*RST', address_2182A, bin_path)

# Select function: ‘VOLTage’ or ‘TEMPerature’.
send_GPIB('\":sens:func \'volt\'\"', address_2182A, bin_path)

# Select channel: 0 (internal temperature sensor), 1, or 2.
send_GPIB('\":sens:chan 1\"', address_2182A, bin_path)

# Select channel 1 measure range; <n> = range.
# DCV1 function has five measurement ranges: 10mV, 100mV, 1V, 10V, and 100V
# DCV2 function has three measurement ranges: 100mV, 1V, and 10V
send_GPIB('\":sens:volt:chan1:rang 1\"', address_2182A, bin_path)

# Enable/disable channel 1 auto range; (ON or OFF).
send_GPIB('\":sens:volt:chan1:rang:auto ON\"', address_2182A, bin_path)

# %% Functions

def v():
    '''
    Reads a voltage value in Volts.

    bin_path and address_2182A variables must be defined already. For example:
        address_2182A = 3
        bin_path = r'D:\amreft-m4p\amreft-m4p_V1_galdino\bin'
    '''

    send_GPIB(':READ?', address_2182A, bin_path)

    return float(receive_GPIB(address_2182A, bin_path))
