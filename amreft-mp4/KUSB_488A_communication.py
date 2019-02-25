# -*- coding: utf-8 -*-
"""
Python 3.7 module to send/receive strings to electronic devices via GPIB using
KUSB-488A:USB to GPIB Interface Adapter.

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

import subprocess
from pathlib import Path

# %% Core functions


def init_gpib():
    '''
    Enable computer to communicate via gpib with address 21

    This must be running nonstop. Run using a thread:

    import threading
    init_thread = threading.Thread(target=init_gpib)
    init_thread.start()
    '''
    subprocess.call(str(Path('../bin/init.exe')), shell=True)
#    os.system('cmd.exe C:/Users/Carlos/Desktop/init.exe')
#    subprocess.call('start cmd C:/Users/Carlos/Desktop/init.exe', shell=True)
#    subprocess.call('cmd C:/Users/Carlos/Desktop/init.exe', shell=True)


def send_GPIB(message, device_address):
    '''
    Send a string via GPIB.
    '''

    # exe path
    func_path = str(Path('../bin/sendGpib.exe'))

    string2send = str(func_path + ' ' + message+' ' + str(device_address))

    sent = str(subprocess.check_output(string2send, shell=True))

    return sent.decode("utf-8")


def receive_GPIB(device_address, bin_path):
    '''
    Receive a message via GPIB
    '''

    # exe path
    func_path = str(Path('../bin/receiveGpib.exe'))

    string2receive = str(func_path + ' ' + str(device_address))

    received = str(subprocess.check_output(string2receive, shell=True))

    return received.decode("utf-8")

# %% Tests

#subprocess.call('C:/Users/Carlos/Desktop/sendGpib.exe *idn? 3', shell=True)
#
#subprocess.call('C:/Users/Carlos/Desktop/receiveGpib.exe 3', shell=True)
#
#sent1 = str(subprocess.check_output('C:/Users/Carlos/Desktop/sendGpib.exe *idn? 3', shell=True))
#out1 = str(subprocess.check_output('C:/Users/Carlos/Desktop/receiveGpib.exe 3', shell=True))
