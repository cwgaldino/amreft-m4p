# -*- coding: utf-8 -*-
"""
Set of functions to control Nanovoltimeter Keithley2182A.

Python 3.7

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

import KUSB_488A_communication as gpib

# %% Device class
class Multimeter_34410A():
    """Agilent multimeter 34410A.

    :param address: gpib address of the device.
    """

    def __init__(self, address):
        self.address = address

        # ###### INITIAL CONFIGURATION (Edit acording to your needs) ######
        # # Restore GPIB and remote options to default.
        # gpib.send('*RST', address)
        #
        # # Select function: ‘VOLTage’ or ‘TEMPerature’.
        # gpib.send(":sens:func \'volt\'", address)
        #
        # # Select channel: 0 (internal temperature sensor), 1, or 2.
        # gpib.send(':sens:chan 1', address)
        #
        # # Enable/disable channel 1 auto range; (ON or OFF).
        # gpib.send(':sens:volt:chan1:rang:auto ON', address)
        #
        # # Select channel 1 measure range; <n> = range.
        # # DCV1 function has five measurement ranges: 10mV, 100mV, 1V, 10V, and 100V
        # # DCV2 function has three measurement ranges: 100mV, 1V, and 10V
        # # gpib.send('\":sens:volt:chan1:rang 1\"', address)

    def clear(self):
        """Clear error."""
        gpib.send('*CLS', self.address)

    def v(self):
        """Read voltage (Volts)."""

        gpib.send("MEAS:VOLT:DC?", self.address)

        try:
            return float(gpib.receive(self.address))
        except ValueError:
            print('ERROR: Communication lost.')
