import os
import datetime
from pytz import timezone

os.system("sudo airmon-ng start wlan1")


timestamp = str(datetime.datetime.now(timezone('Asia/Kolkata')))
newstamp = ""

for i in range(len(timestamp)):
        if timestamp[i] == "." or timestamp[i]== ":" or timestamp[i]== " ":
                newstamp = newstamp + "_"
        else:
                newstamp = newstamp + timestamp[i]


os.system("sudo python probemon4.py -i wlan1mon -o logs/"+newstamp+" -f -r -s -l")
