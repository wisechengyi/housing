import json
from pprint import pprint
import csv

import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# raw = json.load(open('evictions.json', 'r'))
# reader = csv.reader(open('Eviction_Notices.csv', 'r'))
# for row in reader:
#   print row

# def compare_date(a, b):
#   return cmp(datetime.datetime.strptime(a[0], '%m/%d/%Y'), datetime.datetime.strptime(b[0], '%m/%d/%Y'))

def to_year_month(s):
  dt = datetime.datetime.strptime(s, '%m/%d/%Y')
  return datetime.datetime(year=dt.year, month=dt.month, day=1)


df = pd.read_csv('Eviction_Notices.csv', low_memory=False)

df['datetime'] = pd.Series(map(lambda x: to_year_month(x), df['File Date']))
grouped = df.groupby('datetime')

times = map(lambda x: x[0], grouped)
counts = map(lambda x: x[1].count()['datetime'], grouped)
plt.grid(True, which='major')
plt.plot(times, counts)
# plt.show()

x = 5
