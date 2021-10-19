import urllib.request
from time import time

urls = ['https://www.cnn.com/','https://www.facebook.com/']
loadTime = []
for  x in urls:
	stream = urllib.request.urlopen(urls[1])
	start_time = time()
	output = stream.read()
	end_time = time()
	stream.close()
	loadTime.append(round((end_time-start_time),3))
print(loadTime)
