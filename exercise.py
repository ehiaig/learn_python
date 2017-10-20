import random
"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

SOLUTIOn
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))
"""

"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

SOLUTION:
x=int(input("Enter number: "))
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print (fact(x))

#OR

i = int(input("Enter number: "))
total = 1
while i >= 1:
    if i > 1:
        total *= i
        i -= 1
    else:
        break
print(total)

#OR
x=int(input("Enter number: "))
n = 1

for num in range(1, x):
    n = n * x
    x = x-1
print(n)

#OR
while x > 0:
    n = n * x
    x = x - 1
print(n)

"""


"""
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

SOLUTION:
num = int(input("Enter number"))
new_dict = {} #OR new_dict = dict(). This also converts the variable to a dictionary
for n in range(1, num+1):
    new_dict[n] = n *n
print(new_dict)
"""

"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

SOLUTION:
i = input("Enter numbers:")
i = i.split(',')
print(list(i))
print(tuple(i))
"""

a = ['ag', 'hg', 'gdg', 'hgh']
# for n in enumerate(a):
for n in enumerate(a):
    print(n)
for key, value in enumerate(a):
    print(key, value)

#enumerate is used to iterate over list, and text. The output is usually a tuple with index and value

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