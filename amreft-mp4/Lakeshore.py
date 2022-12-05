# -*- coding: utf-8 -*-
"""
Set of functions to control Lakeshore 340 temperature controller.

Python 3.7

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

import KUSB_488A_communication as gpib


class Lakeshore_340():
    """Lakeshore 340 temperature controller."""

    def __init__(self, address):
        self.address = address

         # Configure Control Loop Parameters
        gpib.send('\"CSET 1 A 1 on\"', self.address)
        self.input = 'A'
        self.controlLoop = '1'


    def heater_range(self, *args):
        """Set and get heater range

        heater_range() >> Query Heater Range.
        heater_range(0-5) >> Configure Heater Range (from 0 to 5).

        :params range: heater range.

        :Return: the heater range.
        """
        # if len(args)==1:
        #     gpib.send('\"Range ' + str(args[0]) + '\"', self.address)
        # else:
        #     gpib.send('RANGE?', self.address)
        #     return float(gpib.receive(self.address))
        if len(args)==1:
            gpib.send('\"RANGE ' + str(args[0]) + '\"', self.address)
        else:
            gpib.send('RANGE?', self.address)
            try:
                return float(gpib.receive(self.address))
            except ValueError:
                print('ERROR: Communication lost.')


    def heater_output(self):
        """Get Heater Output (0 to 100%).

        :Return: heater output in percent.
        """
        # gpib.send('HTR?', self.address)
        # return float(gpib.receive(self.address))
        if len(args)==1:
            gpib.send('\"MOUT ' + self.controlLoop + ', ' + str(args[0]) + '\"', self.address)
        else:
            gpib.send('HTR?', self.address)
            try:
                return float(gpib.receive(self.address))
            except ValueError:
                print('ERROR: Communication lost.')

    def get_setpoint(self):
        """Get Control Loop Setpoint.

        :Return: Returns the control loop setpoint.
        """
        gpib.send('\"SETP? ' + self.controlLoop + '\"', self.address)
        # return float(gpib.receive(self.address))
        try:
            return float(gpib.receive(self.address))
        except ValueError:
            print('ERROR: Communication lost.')

    def t(self, *args):
        """Set/get temperature.

        t() queries temperature.
        t(setpoint) sets the setpoint temperature of the selected input.

        :params setpoint: temperature setpoint in Kelvin.
        """

        # if len(args)==1:
        #     gpib.send('\"SETP ' + self.controlLoop + ', ' + str(args[0]) + '\"', self.address)
        # else:
        #     gpib.send('\"KRDG? ' + self.input + '\"', self.address)
        #     return float(gpib.receive(self.address))

        if len(args)==1:
            gpib.send('\"SETP ' + self.controlLoop + ', ' + str('{:.3f}'.format(float(args[0]))) + '\"', self.address)
        else:
            gpib.send('\"KRDG? ' + self.input + '\"', self.address)
            try:
                return float(gpib.receive(self.address))
            except ValueError:
                print('ERROR: Communication lost.')
