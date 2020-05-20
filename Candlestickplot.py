# From pylab example in the matplotlib website
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, \
DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc

#date1 = (2004, 2, 1)
#date2 = (2004, 4, 12)


quotes = quotes_historical_yahoo_ohlc('INTC', date1, date2)

mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')

fig, ax = plt.subplots()
fig.subplots_adjust(bottom = 0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)

candlestick_ohlc(ax, quotes, width = 0.6)
ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation = 45,
         horizontalalignment = 'right')

plt.show()

