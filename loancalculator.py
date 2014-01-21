#!/bin/python
import matplotlib.pyplot as plt
import numpy as np
import os


def monthlypmt(P, apr, yrs):
    # P: amount borrowed
    # apr: yearly interest rate as decimal
    # yrs: loan duration in years
    N = yrs * 12
    r = apr / 100. / 12

    # Calculate monthly payment
    num = P * r * (1+r)**N
    denom = (1+r)**N - 1
    c = num/denom

    # Display some information on screen
    os.system('clear')
    print "\n"
    print "Starting principal is $%.2f" % P
    print "Fixed annual interest rate is %s" % (apr)
    print "Principal + Interest Payment is: $%.2f" % c
    print "Interest paid over life of loan $%.2f" % (c * N - P)
    print "\n"

    # Find remaining balance at each month - amortization formula
    mos = np.arange(N+1)
    num = (1 + r)**mos - 1
    denom = (1 + r)**N - 1
    remaining = P * (1 - num / denom)

    # Break down monthly payment into interest and principal
    intpaid = remaining * r
    pncpaid = c - intpaid

    # Display cumulative interest paid over time
    for month, totint in zip(mos, np.cumsum(intpaid)):
        print month, totint

    # Show some plots
    if 1:
        # Show plots as a function of time in months
        plt.plot(mos, intpaid, label='interest')
        plt.plot(mos, pncpaid, label='principal')
        plt.plot(mos, remaining/1000, label='remaining balance in 1k')
        plt.xlabel('Months')
        plt.ylabel('Payment amount')
        plt.title('Total payment amount is $%.2f' % c)
        plt.legend()
        plt.show()

    return


monthlypmt(10000, 6.25, 10)
