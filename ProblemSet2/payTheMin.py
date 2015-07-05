balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12.0
totalPaid = 0
for i in range(1,13):
	minMonthlyPayment = balance * monthlyPaymentRate
	upBalance = balance - minMonthlyPayment
	balance = upBalance  + upBalance*monthlyInterestRate
	totalPaid +=minMonthlyPayment
	print "Month: %d" % i
	print "Minimum monthly payment: %.2f" % minMonthlyPayment
	print "Remaining balance: %.2f" % balance
print "Total paid:%.2f" % totalPaid
print "Remaining balance: %.2f" % balance
