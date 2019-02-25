===========
amreft-m4p
===========
:Author: Carlos Galdino <galdino@ifi.unicamp.br> and George Kontogiorgos <gekontogiorgos@gmail.com>
:Description: Set of python 3.7 scripts to control electronic devices via GPIB using KUSB-488A:USB to GPIB Interface Adapter


Instructions for the Impatient
-------------------------------
-test0
-test1


Instructions for dummies
-------------------------


Installing and testing keithley GPIB/USB drive
***********************************************

Download, extract, and install the keithley GPIB drive. Here is the link to download: https://www.tek.com/accessory/gpib488/9-2-0, or you may use the zip folder Keithley_GPIB488v92.zip from the projects folder.


.. image:: docs/images/01.png

Restart the computer, connect the Keithley USB/GPIB converter to the computer and Keithley device and open the program TRTEST.

.. image:: docs/images/02.png

If the converter (or any other board is detected) the TRTEST buttons are enabled

.. image:: docs/images/03.png

Click on Initialize and type the computer GPIB address, which we will select as 21.

.. image:: docs/images/04.png

To send a command, check the GPIB address in the Keithley device (In this case it is 03) and click on Send. Send the command *idn?

Note the REM (from remote) lights up at the Keithley screen. Also note the LST (from listening) lights up as an indicative that the device is waiting from the computer the read a response.


.. image:: docs/images/05.png
.. image:: docs/images/06.png

This command asks what is the device name. The device will answer to the question. To check its answer click on Enter and type the device address, then OK.

.. image:: docs/images/07.png
.. image:: docs/images/08.png


Basic communication scripts
***********************************************

WARNING: This section intends to show how to compile (and modify) the C scripts that enables the GPIB communication.  You may skip to the next section if the bin folder has these three files: init.exe, receiveGpib.exe, and sendGpib.exe.

The core communication between the computer and the device is easier if done in C. Download and install MinGW (http://www.mingw.org/), which is a minimalist development environment for native Microsoft Windows applications. Instal it at C:/MinGW


.. image:: docs/images/09.png
.. image:: docs/images/10.png
.. image:: docs/images/11.png
.. image:: docs/images/12.png
.. image:: docs/images/13.png

After installation put MinGW/bin to the windows PATH. This makes possible to run MinGW commands from the prompt from any folder. Open the prompt and type gcc, if a fatal error occur, then the installation was successful.

.. image:: docs/images/14.png
.. image:: docs/images/15.png
.. image:: docs/images/16.png
.. image:: docs/images/17.png

There are 3 C scripts that must be compiled: init.c, receiveGpib.c, and sendGpib.c. If it is necessary to modify this C scripts I recommend downloading the Notepad++, which is just a text editor with text highlight functionality. However, any text editor will do the job.

.. image:: docs/images/18.png









