#!/usr/bin/python

# File	: interest.py
# Date	: May 25, 2017
# Author: Mayur B.

# Import necessary modules here.
import math

# Let's gather required data.
# 1. Principle amound (p)
# 2. Interest Rate (r)
# 3. Compounded per year (n)
# 4. Period (m)

def getInterest(p,r,m,n):
	interest = p*((1+(float(r)/n))**(m*n))
	return interest

def main():
	p = float(raw_input('Enter Principle: '))
	r = float(raw_input('Enter interest rate: '))/100.0
	m = int(raw_input('Enter years: '))
	n = int(raw_input('How many times Compounded a year: '))

	i = getInterest(p,r,m,n)
	print('Total balance would be: {bal}'.format(bal=i))
	print 'Thank you!'

if __name__=='__main__':
	main()