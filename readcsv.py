import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime


def sortedcsv(file, key):

    # Read in CSV data as list of dictionaries
    with open(file, 'rb') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Operations on each row
    for row in rows:

        # Convert date string to date object
        row['Date'] = datetime.datetime.strptime(row['Date'], "%m/%d/%Y")

        # Credit transaction are positive, Debit are negative
        if row['Transaction Type'] == 'debit':
            row['Amount'] = np.float(row['Amount']) * -1
        elif row['Transaction Type'] == 'credit':
            row['Amount'] = np.float(row['Amount']) * +1

    # Sort transaction according to date
    keysorted = sorted(rows, key=lambda field: field[key])

    x = []
    y = []
    for row in keysorted:
        # print '%s -- %s' % (row['Date'], row['Amount'])
        x.append(row['Date'])
        y.append(row['Amount'])

    return x, y


x, y = sortedcsv('transactions.csv', 'Date')

# Create figure and maximize
plt.figure()
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

# Plot values
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0))

# Axes preferences
ax1.bar(x, y, edgecolor='red')
ax1.set_ylabel('Transaction Amount')
ax1.axhline(0, color='black')

ax2.plot(x, np.cumsum(y), '.-')
ax2.set_xlabel('Date')
ax2.set_ylabel('Running Total')

plt.show()
