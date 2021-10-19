from ftplib import FTP
import time
import os
import configparser
import sys

if __name__ == "__main__":
    it=0
    file2Down="50MBdown.zip"
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
            file = open(file2Down,'wb')
            ftp.sendcmd('SIZE '+file2Down)
            time1=time.time()
            print("******Download in Progress******")
            #ftp.retrbinary("RETR "+file2Down,file.write)
            ftp.retrbinary("RETR "+file2Down,file.write)
            time2=time.time()
            print(":) Successful Transmission :)")
            timeDiff = time2 - time1
            speeds = 50*8/timeDiff
            print("Speed: ",speeds,"Mbps")
            os.listdir(path='.')
            file.close()
            try:
                os.remove(file2Down)
            except Exception as e:
                print(e)
            time.sleep(timeToHold)
        except Exception as e:
            print("Error while Downloading")
        it+=1
    ftp.close()
