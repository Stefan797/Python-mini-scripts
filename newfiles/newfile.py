import sys

# check for arguments

print(sys.argv[0]) # prints python_script.py
print(sys.argv[1]) # prints var1 Content
print(sys.argv[2]) # prints var1 Content
print(sys.argv[len(sys.argv) - 1]) # print File Name

name = sys.argv[1]
category = sys.argv[2] # html
content = sys.argv[len(sys.argv) - 1] # index
path = 'C:/Users/Stefan/Desktop/' # change path to desired destination 

with open(path + name + "." + category, "a") as file:
    file.write(content + "\n")

input('Drücke eine beliebige Taste um das Programm zu schließen')