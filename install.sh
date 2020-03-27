sudo apt-get update

echo "\nDownloading and installing gphoto2...\n"

sudo apt-get install gphoto2

sudo apt-get install python3-pip

sudo python3 -m pip install sh

echo "\nDownloading and installing pyBluez...\n" 

sudo apt-get install libbluetooth-dev python-dev libglib2.0-dev libboost-python-dev libboost-thread-dev

pip3 download gattlib
tar xvzf ./gattlib-*.tar.gz # Adapter le nom du fichier selon la version : TAB
cd gattlib-*/				# Pareil
sed -ie 's/boost_python-py34/boost_python-py35/' setup.py
pip3 install .

cd ..

sudo python3 -m pip install pybluez pybluez\[ble\]

echo "\nConfiguring..."

echo "\nEdit line 'ExecStart=/usr/libexec/bluetooth/bluetoothd' : append with '--compat'\n"

sudo systemctl edit --full bluetooth.service

echo "\nInitializing autorun...\n"

sudo chmod +x /home/pi/initDSLRController.sh

echo 'sudo bash /home/pi/initDSLRController.sh' >> /home/pi/.bashrc

echo "\nInstallation completed!\n"
echo "\nThe system will reboot\n"

sudo reboot
