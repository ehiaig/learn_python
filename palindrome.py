import random
"""
#Solve for a palindrome
word = str(input('Enter a word: '))
reverse = word[::-1]

print(reverse)
if word == reverse:
    print('Your input is a palindrome')
else:
    print('Your input is not a palindrome')
"""

"""
Create a list that prints only the even numbers of the list below
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in a:
    if i%2 ==0:
        print (i)
"""

"""
Generate a password with length "passlen" with no duplicate characters in the password

Solution:
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen))
print (p)
"""

"""
Question:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
"""
text = (input('Enter two lines:'))

print(text.upper())