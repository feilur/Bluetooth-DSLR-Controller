# Bluetooth-DSLR-Controller

	v0.0.1

Plug a Raspberry Pi on your DSLR and control it with your smartphone!

/!\ Developped and tested with a Canon EOS 40D and a Raspberry Pi3 with Raspbian Buster Lite (no desktop).

The application to control is not yet developped : it was tested with "Bluetooth Electronics" available on Google Play (send a 'c' with a button to capture)

		/// FEATURES \\\

This version is the foundation of future versions.

- Capture a picture by sending 'c'

Future features :

- Switching to BLE (to be compatible with in-dev app)

- Display and set capture mode (Av, Tv, M)

- Set (or not) self-timer

- Display and set aperture, speed, ISO (bulb mode ?)

- Timelapse mode

? Autofocus or adjust manually focus

? Preview mode


		/// INSTALLATION \\\
		

- Flash Raspbian Buster Lite on your Raspberry Pi

- Copy install.sh, initDSLRController.sh and DSLRController.py on /home/pi (make sure you have an internet access)
	
- Execute install.sh

- Wait untill a file is opened to be edited

- Edit line 'ExecStart=/usr/libexec/bluetooth/bluetoothd' : append with '--compat'

- Press Ctrl+x, then y, then Enter

- The installation will continue then the system will reboot

- If everything is ok, initDSLRController.sh then DSLRController should launch

- Pair your phone in the Bluetooth menu and connect with an application that use serial communication.

	Warning : Plug your DSLR on the Raspberry Pi before connecting your phone by Bluetooth

