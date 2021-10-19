import subprocess
import string
import re

out = subprocess.Popen(['speedtest-cli'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
stdout,stderr=out.communicate()
string = stdout.decode("utf-8")
print(string)
if stderr is None:
    results = [int(s) for s in re.findall(r'\b\d+\b',string)]
    print(results)
    length = len(results)
    if length != 0:
        downSpeed = float(str(results[length-4])+"."+str(results[length-3]))
        uploadSpeed = float(str(results[length-2])+"."+str(results[length-1]))
        print("Downlink: {}".format(downSpeed))
        print("Uplink: {}".format(uploadSpeed))
else:
    print("Speedtest-cli doesn't seem to work!")
