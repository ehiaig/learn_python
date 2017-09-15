#Functions are repeatable blocks of code that performs specific actions
#The function below prints 'I am beautiful 5 times
"""
def compliment():
    print("I am beautiful")

for i in range(5):
    compliment()

#Another
def compliment(name):
    print("{} is beautiful".format(name))

for i in range(6):
    compliment("Francis")

#Yet another
def compliment_me(name, adjective):
    print("{} is {}".format(name, adjective))

for i in range(6):
    compliment_me("Francis", "adjective")

#HH
def compl_me(name):
    return "I dislike {}".format(name)
print(compl_me("Ghana Kenke"))


#Implement a function that returns the function get_prime of prime numbers between 2010 and 3050 inclusive
def get_prime(start, end):
    my_primes = []
    for num in range(start, end+1):
        is_prime = True
        for i in range(2,num):
            if (num%i==0):
                is_prime = False
        if is_prime:
            my_primes.append(num)
    return my_primes
print (get_prime(2050, 3051))

#
def compl_me(name, adjective):
    return "I {} {}".format(adjective, name)
print (compl_me(adjective="love", name="Francis"))

#We want to pass in many variable arguments as possible
def compli_everyone(*args):
    for arg in args:
        print("I love {}".format(arg))
compli_everyone("Francis", "Andrew", "Pascal")

#Write a function that will sum a list of ints
import math
def add_num(*args):
    total = 0
    for num in args:
        total = total + num
    return total
print(add_num(2,3,4,78))
"""
import math
#Find the largest and smallest number of a turple
def large_small(*args):
    is_small = math.inf
    is_large = -math.inf

    for num in args:
        if (num >= is_large):
            is_large = num
        elif (num <= is_small):
            is_small = num
    print("The smalest number is {}".format(is_small))
    print("The largest number is {}".format(is_large))
print(large_small(1,3,-2,7, 8))