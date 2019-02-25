# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:52:09 2019

@author: Carlos galdino
galdino@ifi.unicamp.br
"""

# Enable threading of processes
import threading
# Need to run exe files inside python environment
import subprocess
# Deal with file paths easily
from pathlib import Path


# %% Core functions


def init_gpib():
    '''
    Enable computer to communicate via gpib with address 21

    This must be running nonstop. Run using a thread:

    init_thread = threading.Thread(target=init_gpib)
    init_thread.start()
    '''
    subprocess.call('C:/Users/Carlos/Desktop/init.exe', shell=True)
#    os.system('cmd.exe C:/Users/Carlos/Desktop/init.exe')
#    subprocess.call('start cmd C:/Users/Carlos/Desktop/init.exe', shell=True)
#    subprocess.call('cmd C:/Users/Carlos/Desktop/init.exe', shell=True)


def send_GPIB(message, device_address, bin_path):
    '''
    Send a string via GPIB.
    '''

    # Deal with exe path
    p = Path(bin_path)
    p = p / 'sendGpib.exe'
    func_path = str(p)

    string2send = str(func_path + ' ' + message+' ' + str(device_address))

    sent = str(subprocess.check_output(string2send, shell=True))

    return sent[2:-1]


def receive_GPIB(device_address, bin_path):
    '''
    Receive a message via GPIB
    '''

    # Deal with exe path
    p = Path(bin_path)
    p = p / 'receiveGpib.exe'
    func_path = str(p)

    string2receive = str(func_path + ' ' + str(device_address))

    received = str(subprocess.check_output(string2receive, shell=True))

    return received[2:-1]



# %% Initizalize communication

init_thread = threading.Thread(target=init_gpib)
init_thread.start()

#threading.active_count()
#init_thread.isAlive()


# %%
bin_path = r'D:\amreft-m4p\amreft-m4p_V1_galdino\bin'

sent1 = send_GPIB('*idn?', 3, bin_path)
received1 = receive_GPIB(3, bin_path)


# %%


subprocess.call('C:/Users/Carlos/Desktop/sendGpib.exe *idn? 3', shell=True)

subprocess.call('C:/Users/Carlos/Desktop/receiveGpib.exe 3', shell=True)

sent1 = str(subprocess.check_output('C:/Users/Carlos/Desktop/sendGpib.exe *idn? 3', shell=True))
out1 = str(subprocess.check_output('C:/Users/Carlos/Desktop/receiveGpib.exe 3', shell=True))
