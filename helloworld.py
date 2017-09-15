"""
Problem: Get the computer to output a message.
Target Users: Me
Target System: GNU/Linux
Interface: Command-line
Functional Requirements: Print out a message.
User must be able to input some text.
Testing: Simple run test - expecting a message to appear.
- expecting: message == input text
Maintainer: maintainer@website.com
"""
# 1. Print out a friendly message
print("Hello World!")
# 2. Input some text
sometext = input('Type in some words: ')
# 3. Print out the text we just entered
print(sometext)

#We can import this file as a package of it's own. First we cd into the path in out terminal, than use type "import helloworld". This will turn the file as a manual. We can see the manual by using "help helloworld"

#OR
for line in range(1,4):
     #print("line {}".format(line))
     for space in range(3-line):
         print(" ", end="")

     for stars in range(2*line-1):
         print("*", end="")
     print("")

