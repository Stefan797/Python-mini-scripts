import sys

# check for arguments

print(sys.argv[0]) # prints python_script.py
print(sys.argv[1]) # prints var1 Content
print(sys.argv[2]) # prints var1 Content
print(sys.argv[len(sys.argv) - 1]) # print File Name


content = sys.argv[1]
descrition = sys.argv[2]
name = sys.argv[len(sys.argv) - 1]
path = 'C:/Users/Stefan/Desktop/Developer Akademie Backend/Befehlsübersichten/'

with open(path + name + ".txt", "a") as file:
    file.write(descrition + content + "\n")
