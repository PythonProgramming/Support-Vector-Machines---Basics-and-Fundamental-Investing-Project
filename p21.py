# import urllib.request # python 3
import requests
import os
import time

# path = "X:/Backups/intraQuarter" # for Windows with X files :)
# if git clone'ed then use relative path,
# assuming you extracted the downloaded zip into this project's folder:
path = "intraQuarter"

def Check_Yahoo():
  # headers = {} # may be required in the future
  statspath = path+'/_KeyStats'
  stock_list = [x[0] for x in os.walk(statspath)]
  for e in stock_list[1:]:
    try:
      # ticker = e.replace("X:/Backups/intraQuarter","")
      ticker = os.path.basename(os.path.normpath(e))
      link = "http://finance.yahoo.com/q/ks?s=" + ticker.upper() + "+Key+Statistics"
      # resp = urllib.request.urlopen(link).read()
      resp = requests.get(link)
      save = "forward/" + str(ticker) + ".html"
      store = open(save, "w")
      store.write( str(resp.text) )
      store.close()
      print("Saved: %s" % ticker)
    except Exception as err:
      print(str(err))
      time.sleep(2)

Check_Yahoo()
