balance = 3329
annualInterestRate = 0.2

monthlyInterest = annualInterestRate / 12
minFixedMonthlyPayment = 0
unpaid = balance
while unpaid > 0:
	minFixedMonthlyPayment += 10
	unpaid = balance
	for i in range(1,13):
		unpaid = unpaid - minFixedMonthlyPayment
		unpaid = unpaid * (1 + monthlyInterest)
	

print "Lowest Payment: %d" % minFixedMonthlyPayment
