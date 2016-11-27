#Try to make a script that converts Celsius to Fahrenheit and creates a text file and stores the converted values inside the text file. Your text file content should look like this:
#50.0
#-4.0
#212.0
#Please don't write any message in the text file when input is lower than -273.15.
def convert_c_to_f(c):
    if c > -273.16:
        f=c*9/5+32
        return f


temperatures=[10,-20,-289,100]

def convert(temperatures):
    with open('temperature.txt', 'w') as file:
        for t in temperatures:
            if t > -273.16:
                f=t*9/5+32
                file.write(str(f)+"\n")
                
convert(temperatures)

print("Opening file...\n")
file=open("temperature.txt", 'r')
content=file.read()
print("Reading file...")
print(content)
file.close()
print("Closing file...\n")


