sudo apt-get update

echo "Downloading and installing gphoto2..."

sudo apt-get install gphoto2

sudo apt-get install python3-pip

sudo python3 -m pip install sh

echo "Downloading and installing pyBluez..." 

sudo apt-get install libbluetooth-dev python-dev libglib2.0-dev libboost-python-dev libboost-thread-dev

pip3 download gattlib
tar xvzf ./gattlib-*.tar.gz
cd gattlib-*/				
sed -ie 's/boost_python-py34/boost_python-py35/' setup.py
pip3 install .

cd ..

sudo python3 -m pip install pybluez pybluez\[ble\]

echo "Configuring..."

echo "Edit line 'ExecStart=/usr/libexec/bluetooth/bluetoothd' : append with '--compat'"

sudo systemctl edit --full bluetooth.service

echo "Initializing autorun..."

sudo chmod +x /home/pi/initDSLRController.sh

echo 'sudo bash /home/pi/initDSLRController.sh' >> /home/pi/.bashrc

echo "Installation completed!"
echo "The system will reboot"

sudo reboot
