# -*- coding: utf-8 -*-
"""
Set of functions to control Nanovoltimeter Keithley2182A.

Python 3.7

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

import KUSB_488A_communication as gpib


class CurrentSource_6221():
    """Keithley Current Source Keithley 6221.

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

    def wave_arm(self):
        """Arm waveform function."""
        return gpib.send('SOUR:WAVE:ARM', self.address)

    def wave_initialize(self):
        """Start waveform output."""
        return gpib.send('SOUR:WAVE:INIT', self.address)

    def wave_stop(self):
        """Abort waveform output."""
        return gpib.send('SOUR:WAVE:ABORT', self.address)

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

    def auto_range_ON(self):
        """Enables source autorange."""
        return gpib.send('CURR:RANG:AUTO ON', self.address)

    def auto_range_OFF(self):
        """Disables source autorange."""
        return gpib.send('CURR:RANG:AUTO OFF', self.address)

    def clear(self):
        """Turns output off and sets output level to zero."""
        return gpib.send('CLE', self.address)

    def set_range(self, value):
        """Set current range in Ampere.

        Selecting a fixed source range disables autorange.
        Ranges: 2nA, 2µA, 2mA, 20nA, 20µA, 20mA, 200nA, 200µA, 100mA

        :params value: Current range in Amps.
        """
        return gpib.send('CURR:RANG '+ str(value), self.address)

    def set_compliance(self, value):
        """Set voltage compliance in volts.

        The voltage compliance limit can be set from 0.1V to 105V in 10mV steps

        :params value: Voltage compliance value in volts.
        """
        return gpib.send('CURR:COMP '+ str(value), self.address)

    def set_A(self, value):
        """Set current in Ampere.

        :params value: Output current value in Amps.
        """
        return gpib.send('CURR '+ str(value), self.address)


class Nanovoltimeter_2182A():
    """Keithley nanovoltimeter 2182A.

    :param address: gpib address of the device.
    """

    def __init__(self, address):
        self.address = address

        ###### INITIAL CONFIGURATION (Edit acording to your needs) ######
        # Restore GPIB and remote options to default.
        gpib.send('*RST', address)

        # Select function: ‘VOLTage’ or ‘TEMPerature’.
        gpib.send(":sens:func \'volt\'", address)

        # Select channel: 0 (internal temperature sensor), 1, or 2.
        gpib.send(':sens:chan 1', address)

        # Enable/disable channel 1 auto range; (ON or OFF).
        gpib.send(':sens:volt:chan1:rang:auto ON', address)

        # Select channel 1 measure range; <n> = range.
        # DCV1 function has five measurement ranges: 10mV, 100mV, 1V, 10V, and 100V
        # DCV2 function has three measurement ranges: 100mV, 1V, and 10V
        # gpib.send('\":sens:volt:chan1:rang 1\"', address)

    def v(self):
        """Read voltage (Volts)."""

        gpib.send(':READ?', self.address)

        try:
            return float(gpib.receive(self.address))
        except ValueError:
            print('ERROR: Communication lost.')
