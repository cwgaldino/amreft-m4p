# -*- coding: utf-8 -*-
"""
Set of functions to control Current Source Keithley 6221.

Python 3.7

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

from KUSB_488A_communication import init_gpib, terminate_gpib, send_GPIB, receive_GPIB

# %% Initizalize communication

comm_gpib = init_gpib()

# %% Initial definitions

class currentSource_6221():
    '''
    Keithley Current Source Keithley 6221 class.

    .. note: I could have done functions for every and each command, but I think thats overkill.

    .. note: Also, important commands like: ACAL, FILTER, REL, and RATE were not implemented because I think it is safer to apply these by hand.
    '''

    def __init__(self, gpib_address):
        self.gpib_address = gpib_address

    def filter_ON(self):
        '''
        Enables the output analog filter.
        '''
        return send_GPIB('CURR:FILT ON', self.gpib_address)

    def filter_Off(self):
        '''
        Disables the output analog filter.
        '''
        return send_GPIB('CURR:FILT OFF', self.gpib_address)

    def output_resp_FAST(self):
        '''
        Select fast output response speed for 6221.
        '''
        return send_GPIB('OUTP:RESP FAST', self.gpib_address)

    def output_resp_SLOW(self):
        '''
        Select slow output response speed for 6221.
        '''
        return send_GPIB('OUTP:RESP SLOW', self.gpib_address)

    def output_ON(self):
        '''
        Turn output on.
        '''
        return send_GPIB('OUTP ON', self.gpib_address)

    def output_OFF(self):
        '''
        Turn output off.
        '''
        return send_GPIB('OUTP OFF', self.gpib_address)

    def AutoRange_ON(self):
        '''
        Enables source autorange
        '''
        return send_GPIB('CURR:RAN:AUTO ON', self.gpib_address)

    def AutoRange_OFF(self):
        '''
        Disables source autorange
        '''
        return send_GPIB('CURR:RAN:AUTO OFF', self.gpib_address)

    def clear(self):
        '''
        Turns output off and sets output level to zero.
        '''
        return send_GPIB('CLE', self.gpib_address)

    def set_range(self, currentRange):
        '''
        Set current range in Ampere. Selecting a fixed source range disables autorange.
        Ranges: 2nA, 2µA, 2mA, 20nA, 20µA, 20mA, 200nA, 200µA, 100mA

        :params currentRange: Current range in Amps.
        '''
        return send_GPIB('CURR:RANG '+ str(currentRange), self.gpib_address)

    def set_compliance(self, complience):
        '''
        Set voltage complience in volts.

        The voltage compliance limit can be set from 0.1V to 105V in 10mV steps

        :params complience: Voltage complience in volts.
        '''
        return send_GPIB('CURR:COMP '+ str(complience), self.gpib_address)

    def set_A(self, current):
        '''
        Set current in Ampere.

        :params current: Output current in Amps.
        '''
        return send_GPIB('CURR '+ str(current), self.gpib_address)


# %% Initialize nanovoltimeter

address_6221 = 2
K_6221 = currentSource_6221(address_6221)

# %% Set current

K_6221.set_range(12e-3)  # Selects the 20mA range
K_6221.set_A(12e-3)  # Sets the DC output to 12mA
K_6221.set_compliance(10)  # Sets voltage compliance to 10V

# %% Terminate communication

terminate_gpib(comm_gpib)

