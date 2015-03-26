import pandas as pd
import os
from Quandl import Quandl
import time

# auth_tok = "your_auth_here"
auth_tok = open("quandl_auth_tok.txt","r").read()

# path = "X:/Backups/intraQuarter" # for Windows with X files :)
# if git clone'ed then use relative path,
# assuming you extracted the downloaded zip into this project's folder:
path = "intraQuarter"

def Stock_Prices():
  df = pd.DataFrame()

  statspath = path+'/_KeyStats'
  stock_list = [x[0] for x in os.walk(statspath)]
  # print(stock_list)

  for each_dir in stock_list[1:]:
    try:
      # ticker = each_dir.split("\\")[1] # Windows only
      # ticker = each_dir.split("/")[1] # this didn't work so do this:
      ticker = os.path.basename(os.path.normpath(each_dir))
      # print(ticker) # uncomment to verify

      name = "WIKI/"+ticker.upper()
      print(name)
      data = Quandl.get(
        name,
        trim_start = "2000-12-12",
        trim_end = "2014-12-30",
        authtoken=auth_tok
      )
      data[ticker.upper()] = data["Adj. Close"]
      df = pd.concat([df, data[ticker.upper()]], axis = 1)
    except Exception as e:
      # this except is just a simple retry...
      print(str(e))
      time.sleep(10)
      try:
        # ticker = each_dir.split("\\")[1] # Windows only
        # ticker = each_dir.split("/")[1] # this didn't work on *nix so do this:
        ticker = os.path.basename(os.path.normpath(each_dir))
        # print(ticker) # uncomment to verify

        name = "WIKI/"+ticker.upper()
        data = Quandl.get(
          name,
          trim_start = "2000-12-12",
          trim_end = "2014-12-30",
          authtoken=auth_tok
        )
        data[ticker.upper()] = data["Adj. Close"]
        df = pd.concat([df, data[ticker.upper()]], axis = 1)

      except Exception as e:
        print(str(e))

  df.to_csv("stock_prices.csv")
        
Stock_Prices()
