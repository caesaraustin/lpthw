#from sys import argv 

#script, filename = argv

#txt = open(filename)

#print(f"Here's your file{filename}:")
#print(txt.read())

#print("Type the file name again:")
#file_again = input(" ")

#txt_again = open(file_again)

#print(txt_again.read())

from sys import argv 

script, filename = argv

txt = open(filename)

#print(f"Here's your file{filename}:")
#print(txt.read())

filename = input ("file, sir?")
print(txt.read())

print(txt.close())
#print(txt_again.close())