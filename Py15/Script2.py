print('1')
def currency_converter(rate, euros):
	dollars=euros*rate
	return dollars

x = currency_converter(1.45, 2000000)
#print('Value of {0} euros = {1} dollars '.format(euros, dollars))
print(x)

print(" ************************************* ")
for i in (1,2,3):
    print(i+1)

print(" ************************************* ")
a=["Trickier"]
for i in a:
    print(i)
 
print(" ************************************* ")   
lst=["Terribly Tricky"]
for word in lst:
    for letter in word[-6:]:
        print(letter)
