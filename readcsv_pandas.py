import matplotlib.pyplot as plt
import pandas as pd


def sortedcsv(file, key):

    # Read in CSV data using pandas
    data = pd.read_csv(file)

    # Convert date string to date object
    datekey = 'Date'
    data[datekey] = pd.to_datetime(data[datekey])

    # Credit transaction are positive, Debit are negative
    amount = data['Amount']
    data['Amount'] = amount.where(
        data['Transaction Type'] == 'credit', other=-amount)

    # Sort transaction according to key
    data = data.sort([key])

    return data


out = sortedcsv('transactions.csv', 'Date')
out.to_csv('trans_sorted.csv')

x = out['Date']
y = out['Amount']

if 1:
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

    ax2.plot(x, y.cumsum(), '.-')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Running Total')

    plt.show()
