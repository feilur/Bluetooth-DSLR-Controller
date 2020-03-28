from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess
import bluetooth as bt

# Commands
initMemoryCard = ["--set-config","capturetarget=1"]
triggerCommand = ["--trigger-capture"]
getISO = ["--get-config iso"]



## Bluetooth functions ##
def btConnection():
	print("Configuring Bluetooth Socket...")
	server_socket=bt.BluetoothSocket(bt.RFCOMM)
	server_socket.bind(("",bt.PORT_ANY))
	server_socket.listen(1)
	
	port = server_socket.getsockname()[1]
	
	uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
	
	bt.advertise_service(server_socket,"DSLRController",service_id=uuid,service_classes=[bt.SERIAL_PORT_CLASS],profiles=[bt.SERIAL_PORT_PROFILE])
	
	subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
	
	try:
		print("Waiting for a connection on port",port)
		client_socket,address = server_socket.accept()
		print("Accepted connection from ",address,"\n")
	except:
		print("Impossible to accept a connection\n")
	return client_socket, server_socket
	
def btReceive(client_socket,server_socket):
	try:
		char = 'X'
		print("Waiting for an instruction...")
		while char == 'X':
			char = client_socket.recv(1).decode('utf8')
		print("Received character: ",char,"\n")
	except:
		print("Client disconnected")
		client_socket.close()
		server_socket.close()
		client_socket,server_socket = btConnection()	# Try to reconnect
	return client_socket,server_socket,char



## gphoto2 functions ##
def killgphoto2Process():
	p = subprocess.Popen(['ps','-A'], stdout=subprocess.PIPE)
	out, err = p.communicate()
	
	# Search for the line that has the process
	# we want to kill
	for line in out.splitlines():
		if b'gvfsd-gphoto2' in line:
			# Kill the process!
			pid = int(line.split(None,1)[0])
			os.kill(pid, signal.SIGKILL)

def captureImage():
	# Ajouter option d'autofocus avec choix de point (ou pas)
	gp(triggerCommand)

#def changeAperture(close): # True = close, False = open diaphragm


## gphoto2 init ##
print("Killing gphoto2 process...")
killgphoto2Process()
print("gphoto2 process killed!\n")

# Bluetooth init
cs,ss = btConnection()

print("Initializing Memory Card...")
gp(initMemoryCard)
print("Memory Card initialized!\n")

# Main program
instruction = ''
while instruction != 'q':
	cs,ss,instruction = btReceive(cs,ss) # Waiting instruction
			
	if instruction == 'c':
		captureImage()
	elif instruction =='q':
		print("Exiting program...\n")
	else:
		print("Unknown instruction\n")

# gphoto2 --capture-movie --stdout | ffmpeg -i pipe:0 http://localhost:8080/feed1.ffm

cs.close()
ss.close()
