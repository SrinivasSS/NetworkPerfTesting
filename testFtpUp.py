import pysftp
import sys
import time
import os

file_name = "20MBup.zip"
ftp_server = "35.230.21.110"

try:
	sftp = pysftp.Connection(host=ftp_server, username="pi", private_key="/home/pi/ssh-keys")
	print("Connected to cloud ftp server at %s"%(ftp_server))
except:
	print("Cannot connect to FTP server, check credentials...")
try:
	print("Uploading file...")
	time1 = time.time()
	sftp.put("/home/pi/projectSensor/%s"%(file_name),"/home/pi/20MBup.zip")
	time2 = time.time()
	print("Finished")
	upSpeed = 20*8/(time2-time1)
	print("SFTP up speed: ",upSpeed)
except:
	print("Error on uploading file")
sftp.close()

