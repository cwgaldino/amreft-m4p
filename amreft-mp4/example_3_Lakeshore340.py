# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:52:09 2019

@author: Carlos galdino
galdino@ifi.unicamp.br
"""


from galdinoFunctions_gpib_V1.py import *



# %% Initial definitions

address_6221 = 2
bin_path = r'D:\amreft-m4p\amreft-m4p_V1_galdino\bin'

# %% Relevant commands
# I could have done separete functions for each of this commands, but they are
# used only once (or maybe twice) in the script so it is not worthy.

# Reset Instrument
send_GPIB('*RST', address_6221, bin_path)

# Query Heater Output
send_GPIB('HTR?', address_6221, bin_path)

# Query Heater Status
send_GPIB('HTRST?', address_6221, bin_path)

# %% Functions

def t(*argv):
    '''
    t() queries Setpoint temperature.
    t(setpoint) sets the setpoint temperature

    bin_path and address_6221 variables must be defined already. For example:
        address_6221 = 2
        bin_path = r'D:\amreft-m4p\amreft-m4p_V1_galdino\bin'
    '''

    if len(argv)==1:
#        print('het')
        send_GPIB('\"SETP ' + str(args[0]) + '\"', address_6221, bin_path)
    else:
#        print('iii')
        send_GPIB('SETP?', address_6221, bin_path)
        return float(receive_GPIB(address_2182A, bin_path))


