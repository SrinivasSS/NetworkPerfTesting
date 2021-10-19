import subprocess
import string
import re

def testPing():
	count = 15  #Number of pings
	out = subprocess.Popen(['ping','-c',str(count),'cnn.com'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	stdout,stderr=out.communicate()
	string = stdout.decode("utf-8")
	print(string)
	if stderr is None:
	    results = [int(s) for s in re.findall(r'\b\d+\b',string)]
	    print(results)
	    length = len(results)
    	if length != 0:
            jitter = float(str(results[length-2])+"."+str(results[length-1]))
            print("Jitter: {} ms".format(jitter))
            rtt = float(str(results[length-6])+"."+str(results[length-5]))
            print("Avg RTT: {} ms".format(rtt))
            loss = results[length-9]
            print("Packet loss: {}%".format(loss))
	else:
    	    print("Ping doesn't seem to work!")
