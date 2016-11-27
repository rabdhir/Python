print('1')
def currency_converter(rate, euros):
	dollars=euros*rate
	return dollars

x = currency_converter(1.45, 2000000)
#print('Value of {0} euros = {1} dollars '.format(euros, dollars))
#print(x)
function = [currency_converter(1.62, 1000), currency_converter(1.65, 1000)]
print(function)
