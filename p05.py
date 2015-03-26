import pandas as pd
import os
import time
from datetime import datetime

# path = "X:/Backups/intraQuarter" # for Windows with X files :)
# if git clone'ed then use relative path,
# assuming you extracted the downloaded zip into this project's folder:
path = "intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
  statspath = path+'/_KeyStats'
  stock_list = [x[0] for x in os.walk(statspath)]
  for each_dir in stock_list[1:]:
    each_file = os.listdir(each_dir)
    # ticker = each_dir.split("\\")[1] # Windows only
    # ticker = each_dir.split("/")[1] # this didn't work so do this:
    ticker = os.path.basename(os.path.normpath(each_dir))
    # print(ticker) # uncomment to verify
    if len(each_file) > 0:
      for file in each_file:
        date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
        unix_time = time.mktime(date_stamp.timetuple())
        #print(date_stamp, unix_time)
        full_file_path = each_dir+'/'+file
        print(full_file_path)
        source = open(full_file_path,'r').read()
        #print(source)
        value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        print(ticker+":",value)
      # time.sleep(15)
      # 2015jan28: this error occurs: ???
      # intraQuarter/_KeyStats/aapl/20060203134959.html
      # Traceback (most recent call last):
      #   File "p5.py", line 31, in <module>
      #     Key_Stats()
      #   File "p5.py", line 27, in Key_Stats
      #     value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
      # IndexError: list index out of range

Key_Stats()
