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


def initialize():
    """Initialize communication with controller address 21.

    It starts a subprocess that opens the prompt and runs ../bin/init.exe.

    The process run indefinitely and must be terminated by running
    terminate(process)

    Warning: Do not run multiple instances of initialize().

    :return: subprocess.Popen object
    """

    process = subprocess.Popen(str(Path('../bin/init.exe')), shell=True)

    return process
#	 subprocess.call(str(Path('../bin/init.exe')), shell=True)
#    os.system('cmd.exe C:/Users/Carlos/Desktop/init.exe')
#    subprocess.call('start cmd C:/Users/Carlos/Desktop/init.exe', shell=True)
#    subprocess.call('cmd C:/Users/Carlos/Desktop/init.exe', shell=True)


def terminate(process):
    """Terminate communication.

    :param process: A subprocess.Popen object initiated by initialize().
    """
    return subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=process.pid))


def send(message, address):
    """Send message via GPIB.

    :param message: string message to be sent to the device.
    :param address: gpib address of the device.

    :return: message sent.
    """

    # exe path
    func_path = str(Path('../bin/sendGpib.exe'))

    string2send = str(func_path + ' ' + message+' ' + str(address))

    sent = str(subprocess.check_output(string2send, shell=True))

    return sent[2:-1]


def receive(device_address):
    """Receive a message via GPIB.

    :param address: gpib address of the device.

    :return: message received from the device.
    """

    # exe path
    func_path = str(Path('../bin/receiveGpib.exe'))

    string2receive = str(func_path + ' ' + str(address))

    received = str(subprocess.check_output(string2receive, shell=True))

    return received[2:-1]
