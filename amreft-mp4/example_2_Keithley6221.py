# -*- coding: utf-8 -*-
"""
Set of functions to control Current Source Keithley 6221.

Python 3.7

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

import KUSB_488A_communication as gpib

# %% Initizalize communication
comm = initizalize()

# %% Device class
class CurrentSource_6221():
    """Keithley Current Source Keithley 6221 class.

    .. note: Also, important commands like: ACAL, FILTER, REL, and RATE were not implemented because I think it is safer to use these by hand.

    :param address: gpib address of the device.
    """

    def __init__(self, address):
        self.address = address

    def filter_ON(self):
        """Enables the output analog filter."""
        return gpib.send('CURR:FILT ON', self.address)

    def filter_Off(self):
        """Disables the output analog filter."""
        return gpib.send('CURR:FILT OFF', self.address)

    def output_resp_FAST(self):
        """Select fast output response speed for 6221."""
        return gpib.send('OUTP:RESP FAST', self.address)

    def output_resp_SLOW(self):
        """Select slow output response speed for 6221."""
        return gpib.send('OUTP:RESP SLOW', self.address)

    def output_ON(self):
        """Turn output on."""
        return gpib.send('OUTP ON', self.address)

    def output_OFF(self):
        """Turn output off."""
        return gpib.send('OUTP OFF', self.address)

    def AutoRange_ON(self):
        """Enables source autorange."""
        return gpib.send('CURR:RAN:AUTO ON', self.address)

    def AutoRange_OFF(self):
        """Disables source autorange."""
        return gpib.send('CURR:RAN:AUTO OFF', self.address)

    def clear(self):
        """Turns output off and sets output level to zero."""
        return gpib.send('CLE', self.address)

    def set_range(self, currentRange):
        """Set current range in Ampere.

        Selecting a fixed source range disables autorange.
        Ranges: 2nA, 2µA, 2mA, 20nA, 20µA, 20mA, 200nA, 200µA, 100mA

        :params currentRange: Current range in Amps.
        """
        return gpib.send('CURR:RANG '+ str(currentRange), self.address)

    def set_compliance(self, complience):
        """Set voltage complience in volts.

        The voltage compliance limit can be set from 0.1V to 105V in 10mV steps

        :params complience: Voltage complience in volts.
        """
        return gpib.send('CURR:COMP '+ str(complience), self.address)

    def set_A(self, current):
        """Set current in Ampere.

        :params current: Output current in Amps.
        """
        return gpib.send('CURR '+ str(current), self.address)


# %% Initialize nanovoltimeter
address_6221 = 2
K_6221 = CurrentSource_6221(address_6221)

# %% Set current
K_6221.set_range(12e-3)  # Selects the 20mA range
K_6221.set_A(12e-3)  # Sets the DC output to 12mA
K_6221.set_compliance(10)  # Sets voltage compliance to 10V

# %% Terminate communication
gpib.terminate(comm)
