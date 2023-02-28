import os;

home = os.path.expanduser('~') 
os.system(f"pip --disable-pip-version-check list --outdated --format=json >  \"{home}/Documents/Upgrade All.txt\"") #Finding all outdated packages and creating a document with the findings

f = open(f"{home}/Documents/Upgrade All.txt", "r") 
all_needed = f.read() #Reading the document

i = 0 #Where we will store the locatin of the word "name" in the document, as each package name will be mentioned with that keyword
while i != -1: #Until we reach the end of the list of packages
    i = all_needed.find("name") #Find the first "name" keyword 
    all_needed = all_needed[i+8:] #Find the start of the package name
    j = all_needed.find("\"") #Find the end of the package name
    os.system(f"pip install --upgrade {all_needed[0:j]}") #Enter the upgrade order in the terminal

os.remove(f"{home}/Documents/Upgrade All.txt") #Removing the outdated programs document