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

causes = 'Non Payment,Breach,Nuisance,Illegal Use,Failure to Sign Renewal,Access Denial,Unapproved Subtenant,Owner Move In,Demolition,Capital Improvement,Substantial Rehab,Ellis Act WithDrawal,Condo Conversion,Roommate Same Unit,Other Cause,Late Payments,Lead Remediation,Development,Good Samaritan Ends'.split(
  ',')
causes_count = dict(zip(causes, [[] for x in causes]))
for group in grouped:
  sub_total = 0
  for cause in causes:
    count = np.count_nonzero(group[1][cause])
    sub_total = sub_total + count
    causes_count[cause].append(count)

  # if sub_total < group[1].count()['datetime']:
  #   print "suspicious:", group
  #   break

times = map(lambda x: x[0], grouped)
total_counts = map(lambda x: x[1].count()['datetime'], grouped)

plt.grid(True)
# plt.plot(times, total_counts)
colors = [plt.cm.gist_ncar(i) for i in np.linspace(0, 1, len(causes))]
subplots = []
for i in xrange(len(causes)):
  bottom = causes_count[causes[i-1]] if i > 0 else None
  p = plt.bar(times, causes_count[causes[i]], width=20, color=colors[i], bottom=bottom)
  subplots.append(p)

from matplotlib.font_manager import FontProperties

fontP = FontProperties()
fontP.set_size('small')
# legend([plot1], "title", prop=fontP)

plt.legend(subplots, causes, loc='best')

# for cause, count in causes_count.items():
#   plt.bar(times, count, bottom=)
#   break

plt.show()

x = 5
