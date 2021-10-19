from ftplib import FTP
import time
import os
import configparser
import sys

if __name__ == "__main__":
    it=0
    file2Up="50MBup.zip"
    timeToHold=2
    arg_cnt= len(sys.argv)
    if arg_cnt == 1:
        iteration=1
    else:
        iteration=int(sys.argv[1])
    try:
        ftp = FTP('18.206.254.10')
        ftp.login(user='hughesftp', passwd='hughes@456')
    except:
        print("Problem with FTP to server... !!! Check your credentials")
    while it < iteration:
        try:
            print("******Upload in Progress******")
            upload = open(file2Up,'rb')
            time1=time.time()
            ftp.storbinary('STOR {}'.format(file2Up), upload)
            time2=time.time()
            print(":) Successful Transmission :)")
            timeDiff = time2 - time1
            speeds = 50*8/timeDiff
            print("Speed: ",speeds,"Mbps")
            ftp.retrlines('LIST')
            ftp.size(file2Up)
            print("Before Delete")
            ftp.delete(file2Up)
            upload.close()
            time.sleep(timeToHold)
        except Exception as e:
            print("Error while Downloading")
        it+=1
    ftp.close()
