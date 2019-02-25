# -*- coding: utf-8 -*-
"""
Set of functions to control Lakeshore 340 temperature controller.

Python 3.7

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

from KUSB_488A_communication import init_gpib, terminate_gpib, send_GPIB, receive_GPIB

# %% Initizalize communication

comm_gpib = init_gpib()

# %% Device class

class lakeshore_340():
    '''
    Lakeshore 340 temperature controller class.
    '''

    def __init__(self, gpib_address):
        self.gpib_address = gpib_address

         # Configure Control Loop Parameters
        send_GPIB('CSET 1 A 1 on', self.gpib_address)
        self.input = 'A'
        self.controlLoop = '1'


    def heater_range(self, *args):
        '''
        heater_range() >> Query Heater Range.
        heater_range(0-5) >> Configure Heater Range (from 0 to 5).

        :params range: heater range.

        :Return: the heater range.
        '''
        if len(args)==1:
            send_GPIB('Range ' + str(args[0]), self.gpib_address)
        else:
            send_GPIB('RANGE?', self.gpib_address)
            return float(receive_GPIB(self.gpib_address))


    def heater_output(self):
        '''
        Query Heater Output.

        :Return: heater output in percent.
        '''
        send_GPIB('HTR?', self.gpib_address)
        return float(receive_GPIB(self.gpib_address))

    def get_setpoint(self):
        '''
        Query Control Loop Setpoint.

        :Return: Returns the control loop setpoint.
        '''
        send_GPIB('SETP? ' + self.controlLoop, self.gpib_address)
        return float(receive_GPIB(self.gpib_address))

    def t(self, *args):
        '''
        t() queries temperature.
        t(setpoint) sets the setpoint temperature of the selected input.

        :params setpoint: temperature setpoint in Kelvin.
        '''

        if len(args)==1:
            send_GPIB('\"SETP ' + self.controlLoop + ', ' + str(args[0]) + '\"', self.gpib_address)
        else:
            send_GPIB('KRDG? ' + self.input, self.gpib_address)
            return float(receive_GPIB(self.gpib_address))


# %% Initialize lakeshore 340

address_340 = 2
L340 = lakeshore_340(address_340)

# %% Set temperature

L340.t(310)  # set setpoint to 310 K
L340.t()  # Query setpoint
L340.t()  # Query setpoints

# %% Terminate communication

terminate_gpib(comm_gpib)
