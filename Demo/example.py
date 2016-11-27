import datetime

"""
This script creates an empty file.
"""


#filename="sample1.txt"
filename=datetime.datetime.now()

#Create empty file
"""This function creates an empty file"""
def create_file():
    with open(str(filename.strftime("%Y-%m-%d-%H-%M-%S")+".txt"),"w") as file:
        file.write("") #Writing empty string
        
create_file()
