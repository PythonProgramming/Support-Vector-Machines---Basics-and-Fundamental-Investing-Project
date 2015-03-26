import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
from matplotlib import style
style.use("ggplot")

FEATURES =  [
  'DE Ratio',
  'Trailing P/E',
  'Price/Sales',
  'Price/Book',
  'Profit Margin',
  'Operating Margin',
  'Return on Assets',
  'Return on Equity',
  'Revenue Per Share',
  'Market Cap',
  'Enterprise Value',
  'Forward P/E',
  'PEG Ratio',
  'Enterprise Value/Revenue',
  'Enterprise Value/EBITDA',
  'Revenue',
  'Gross Profit',
  'EBITDA',
  'Net Income Avl to Common ',
  'Diluted EPS',
  'Earnings Growth',
  'Revenue Growth',
  'Total Cash',
  'Total Cash Per Share',
  'Total Debt',
  'Current Ratio',
  'Book Value Per Share',
  'Cash Flow',
  'Beta',
  'Held by Insiders',
  'Held by Institutions',
  'Shares Short (as of',
  'Short Ratio',
  'Short % of Float',
  'Shares Short (prior '
]

def Build_Data_Set():
  data_df = pd.DataFrame.from_csv("key_stats.csv")

  # data_df = data_df[:100]

  X = np.array(data_df[FEATURES].values)#.tolist())

  y = ( data_df["Status"]
        .replace("underperform",0)
        .replace("outperform",1)
        .values.tolist()
  )

  X = preprocessing.scale(X)

  return X,y

def Analysis():
  test_size = 1000
  X, y = Build_Data_Set()
  print(len(X))

  clf = svm.SVC(kernel="linear", C=1.0)
  clf.fit(X[:-test_size],y[:-test_size])

  correct_count = 0

  for x in range(1, test_size+1):
    if clf.predict(X[-x])[0] == y[-x]:
      correct_count += 1

  print("correct_count=%s"%correct_count)
  print("test_size=%s"%test_size)
  # on OS X with 64-bit python 2.7.6 had to add float(), otherwise result was zero:
  print("Accuracy:", (float(correct_count) / float(test_size)) * 100.00)

Analysis()
