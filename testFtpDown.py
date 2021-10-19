import pysftp
import sys
import time
import os

file_name = "20MB.zip"
ftp_server = "35.230.21.110"

try:
	sftp = pysftp.Connection(host=ftp_server, username="pi", private_key="/home/pi/ssh-keys")
	print("Connected to cloud ftp server at %s"%(ftp_server))
except:
	print("Cannot connect to FTP server, check credentials...")
try:
	print("Downloading file...")
	time1 = time.time()
	sftp.get("/home/pi/%s"%(file_name),"/home/pi/projectSensor/20MB.zip")
	time2 = time.time()
	print("Finished")
	downSpeed = 20*8/(time2-time1)
	print("SFTP down speed: ",downSpeed)
except:
	print("Error on downloading file")
sftp.close()




