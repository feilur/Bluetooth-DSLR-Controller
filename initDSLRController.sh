echo "Initializing bluetooth..."

sudo service bluetooth restart
sleep 1

sudo sdptool browse local

sudo hciconfig -a hci0 reset

sudo hciconfig hci0 name 'DSLR Controller'

sudo hciconfig -a

sudo hciconfig hci0 piscan

echo "DSLR Controller is launching!"

sudo python3 /home/pi/DSLRController.py
