balance = 320000
annualInterestRate = 0.2
monthlyInterest = annualInterestRate / 12
lowerbound = balance/12.0
upperbound = balance*pow((1+ monthlyInterest),12) /12.0
minFixedMonthlyPayment = (lowerbound + upperbound)/2

while abs(upperbound- lowerbound) >= 0.01:
	unpaid = balance
	for i in range(1,13):
		unpaid = unpaid - minFixedMonthlyPayment
		unpaid = unpaid * (1 + monthlyInterest)
	if unpaid >= 0:
		lowerbound = minFixedMonthlyPayment
	elif unpaid < 0:
 		upperbound = minFixedMonthlyPayment
	minFixedMonthlyPayment = (lowerbound + upperbound)/2
	

print "Lowest Payment: %.2f" % minFixedMonthlyPayment
