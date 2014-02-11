#import the argv library so that the script can take arguments
from sys import argv

#set the parameters for running the script
script, filename = argv

#the txt variable opens the given filename
txt = open(filename)

#prints the name of the file, the contents of the text file
print "Here's your file %r:" % filename
print txt.read()

#allows for reloading the file using raw_input
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()