#This function converts Celsius degrees to Fahrenheit

def convert_Celsius_to_Fahrenheit(Celsius):
	if Celsius < -273.15:
		return "That temperature doesn't make sense! "
	else:
		Fahrenheit = (Celsius * 9/5) + 32
		return Fahrenheit


#print(convert_Celsius_to_Fahrenheit(-275))

#Coding Exercise 3
temperatures=[10,-20,-289,100]
#result=[]
for t in temperatures:
	print(convert_Celsius_to_Fahrenheit(t))
	


