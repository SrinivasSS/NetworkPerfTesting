import speedtest

s = speedtest.Speedtest()
s.get_config()
s.get_best_server()
down_bps = s.download()
up_bps = s.upload()
down_mbps = round(down_bps / 1000 / 1000,2)
up_mbps = round(up_bps / 1000 / 1000,2)
print("Downlink: {} Mbps".format(down_mbps))
print("Uplink: {} Mbps".format(up_mbps))
