# -*- coding: utf-8 -*-
"""
Set of functions to control Nanovoltimeter Keithley2182A.

Python 3.7

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

from KUSB_488A_communication import init_gpib, terminate_gpib, send_GPIB, receive_GPIB

# %% Initizalize communication

comm_gpib = init_gpib()

# %% Device class

class nanovoltimeter_2182A():
    '''
    Keithley nanovoltimeter 2182A class.

    .. note: I could have done functions for every and each command, but I think thats overkill.

    .. note: Also, important commands like: ACAL, FILTER, REL, and RATE were not implemented because I think it is safer to apply these by hand.
    '''

    def __init__(self, gpib_address):
        self.gpib_address = gpib_address

        # INITIAL CONFIGURATION (Edit acording to your needs) =============
        # Restore GPIB and remote options to default.
        send_GPIB('*RST', gpib_address)

        # Select function: ‘VOLTage’ or ‘TEMPerature’.
        send_GPIB('\":sens:func \'volt\'\"', gpib_address)

        # Select channel: 0 (internal temperature sensor), 1, or 2.
        send_GPIB('\":sens:chan 1\"', gpib_address)

        # Enable/disable channel 1 auto range; (ON or OFF).
        send_GPIB('\":sens:volt:chan1:rang:auto ON\"', gpib_address)

        # Select channel 1 measure range; <n> = range.
        # DCV1 function has five measurement ranges: 10mV, 100mV, 1V, 10V, and 100V
        # DCV2 function has three measurement ranges: 100mV, 1V, and 10V
        # send_GPIB('\":sens:volt:chan1:rang 1\"', gpib_address)

    def v(self):
        '''
        Reads a voltage value in Volts.

        :return: measured voltage in volts.
        '''

        send_GPIB(':READ?', self.gpib_address)

        return float(receive_GPIB(self.gpib_address))


# %% Initialize nanovoltimeter

address_2182A = 3
K_2182A = nanovoltimeter_2182A(address_2182A)

# %% Ask voltage

voltage = K_2182A.v()
print(voltage)

# %% Terminate communication

terminate_gpib(comm_gpib)


