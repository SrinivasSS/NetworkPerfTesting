import subprocess
import string
import re

out = subprocess.Popen(['iwconfig','wlan0'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = subprocess.check_output(('grep', 'ESSID\|Quality\|Frequency\|Bit Rate'), stdin=out.stdout, stderr=subprocess.STDOUT)

#print(output)
#stdout,stderr=out.communicate()
string = output.decode("utf-8")
#print("String type",type(string))

if out.stderr is None:
    results = re.split(r'\s+',string)
    print(results)
    length = len(results)
    #print("Length of results: ",length)
    ap_mac = results[9]
    ssid_str = re.split(r':',results[3])
    print("ssid_str: ",ssid_str)
    ssid = ssid_str[1]

    freq_str = re.split(r':',results[5])
    print("freq_str:",freq_str)
    freq = freq_str[1]
    
    quality_str = re.split(r'=',results[16])
    print("\nQuality_str: ",quality_str)
    quality = quality_str[1]

    sigLvl_str = re.split(r'=',results[18])
    sigLvl = sigLvl_str[1]

    print("AP MAC: ",ap_mac) 
    print("SSID: ",ssid)
    print("Frequency: ",freq," Ghz")
    print("Quality: ",quality)
    print("Signal Level: ",sigLvl," dBm")
    #print(length)
    results = [int(s) for s in re.findall(r'\b\d+\b',string)]
    #print(results)
else:
    print("iwlist on interface wlan0 doesn't seem to work!")


