# i = 14

# while i>-2:
#   if i % 2 == 0 and i >= 0:
#     status = "even"
#     print str(i) + " is " + status
#     i = i - 3
#   elif i % 2 !=0 and i>= 0:
#     status = "odd"
#     print str(i) + " is " + status
#     i = i - 3
#   else:
#     status = "negative"
#     print str(i) + " is " + status
#     i = i - 3


# MULTIPLICATION TABLE

# array = range(1,11)

# for num in range (1,11):
#   print map(lambda array: array*num, array)


# MULTIPLICATION TABLE (ALTERNATE SOLUTION)

# for i in range(1,11):
#   print("Multiplication Table for " + str(i) + "'s")
#   for j in range(1,11):
#     product = str(i*j)
#     print(str(i) + " * " + str(j) + " = " + product)

# for i in range(1,13):
#   print("####################### NEXT NEXT NEXT #############################")
#   for j in range(1,13):
#       ans=i*j
#       print(str(i) + " * " +  str(j) + " = " + str(ans))


# INCREMENTAL FOR LOOP
# for num in range(1,10,2):
#   print (num)

# print(range.__doc__)

# NESTED FOR LOOP AND FORMATTING
# for i in range(2):
#   for j in range(3):
#     print("{} * {} = {}".format(i,j,(i*j)))


# CHRISTMAS TREE
# for row in range (3):
#   for space in range (2 - row):
#     print(" ")
#   for star in range(1 + (row * 2)):
#     print("*")
#   print('\n')

# PRINT ALL THE PRIME NUMBERS FROM LOW - HIGH

# def prime_calc(low,high):
#   for number in range(low,high):
#     is_prime = True
#     for divisor in range (2, number):
#       if (number % divisor ==0):
#         is_prime = False
#     if (is_prime):
#       print(number)


# prime_calc(11,100)


# FUNCTION TEST
# def compliment_me(name,adjective):
#   for i in range(5):
#     # print name + " is " + adjective + " loop " + str(i)
#     print("{} is {}".format(name,adjective))
#     return "I {} {}".format(adjective,name)

# # compliment_me("sadiq","strong")
# compliment_me(adjective = "love", name="francis")


# LISTS

# my_nums=[]

# for num in range(2,10,2):
#   my_nums.append(num)
#   print my_nums

# WILDCARD TAKING UNLIMITED VARIABLES

# def compliment_everyone(*args):
#   for arg in args:
#     print("Hello: {}").format(arg)

# compliment_everyone("Jim", "James", "Pascal")

# ADD ALL

# def add_all(*args):
#   sum = 0
#   for arg in args:
#     sum = sum + arg
#   return sum

# add_all(1,2,3,4,-5)

# SQUARE VALUES
# def square_me(*args):
#   array = []
#   for arg in args:
#     array.append(arg**2)
#   return array


# LARGE SMALL

# def large_small(*args):
#   large = small = args[0]
#   for arg in args:
#     if arg > large:
#       large = arg
#     if arg < small:
#       small = arg
#   print small
#   print large

# large_small(1,-4,47,202)


# CHRISTMAS TREE
# for line in range(1,4):
#   # print("line {}".format(line))
#   for spaces in range (3-line):
#     print(" ", end="")
#   for stars in range((2*line) - 1):
#     print("*", end="")
#   print("")#prints a new line

# DIAMONDS
# for line in range(1,4):
#   for spaces in range(3-line):
#     print(" ", end="")
#   for stars in range((2*line) -1):
#     print("*", end="")
#   print("")
# for line in range(5,7):
#   for space in range(line-3):
#     print(" ", end="")
#   for stars in range((-1//2)*line+5+(1//2)):
#     print("*", end="")
#   print("")


# DIAMOND AT HOME
# for line in range(1,6):
#   if line <= 3:
#     for space in range(3 - line):
#       print(" ", end=" ")
#     for star in range(2*line - 1):
#       print("*", end=" ")
#     print("")
#   else:
#     for space in range(line - 3):
#       print(" ", end=" ")
#     for star in range(11 - 2*line):
#       print("*", end=" ")
#     print("")

# DIAMOND (DYNAMIC)

# def diamond(n,shape):
#   for line in range(1,n+1):
#     if line <= (n+1)//2:
#       for space in range(((n+1)//2) - line):
#         print(" ", end=" ")
#       for star in range(2*line - 1):
#         print(shape, end=" ")
#       print("")
#     else:
#       for space in range(line - ((n+1)//2)):
#         print(" ", end=" ")
#       for star in range((2*n+1) - 2*line):
#         print(shape, end=" ")
#       print("")

# diamond(25,"o")


# line = 1
# counter =1
# while line > 0:
#   if line == 3:
#     counter =-1
#     print(line)
#     line+= counter

# name = "Andrew"
# IS_BEAUTIFUL = True
# if(name=="Andrew") and (IS_BEAUTIFUL):
#   print("oh hello, beautiful")


# IS DIVISIBLE

# def even_divisible(start,finish):


#   for num in range(start,finish):

#     def is_even(num):
#       return num % 2 == 0

#     def is_divisible_by_3(num):
#       return num % 3 ==0

#     if is_even(num) and is_divisible_by_3(num):

#       print ("{} is even and divisible by 3".format(num))
# even_divisible(10,99)

# def compliment(message,name="Andrew"):
#   print("{} is {}".format(name,message))

# me = "Sadiq"
# thing_to_say = "so tired of your shit"
# compliment(thing_to_say,me)

# PRINT EVERY OTHER INDEX IN LIST

# def print_every_other(start,finish):
#   for num in range(start,finish,2):
#     print("number is {}".format(num))
# print_every_other(5,10)

# def print_every_other_index(list):
#   for i in range(1,len(list),2):
#     print(list[i])

# print_every_other_index([1,2,10,17,44,-3,4])

# PRINT EVERY OTHER INDEX IN LIST using SLICE
# list = [1,2,3,4,5,6,7,8,9,10]

# print list[1:9:3]
# print list[::-1]
# print list[5:0:-1]
# print list[-2]

# HUMAN AND DOG CHALLENGE
# Put all dogs one step in from of human
# input = "hd..h...d..h.d...h.h"
# for i, letter in enumerate(input):
#   print i,letter
#   if letter == "d" and  input[i-1] != "h":
#     print("come home lassie")
#     ''.join([input[i-1:i+1][::-1] for i in range(0,len(input),1)])

# print ("input is {}".format(input))
# ALTERNATE HUMAN AN DDOG CHALLENGE
# stirr = "hd...h...d..d..hd...h"
# stir = list(stirr)
# line = 0
# while (line < len(stir)):
#   try:
#     if stir[line] == 'h' and not(stir[line+1] == 'd'):
#       #print (stir[line], stir[line + 1])
#       for ch in stir[line + 1:]:
#         if ch == 'd':
#           ch, stir[line +1] = stir[line +1], ch
#   except IndexError:
#     break
#   line = line + 1



# print (''.join(stir))

# JACOB ZUMA CHALLENGE

# sentence = "The dogs and cows were at the barn"
# sentence = sentence.lower().split()
# swear_words = {'the':'t-word', 'and':'a-word', 'cow': 'c-word', 'barn': 'b-word'}
# replaced_input = []

# for word in sentence:
#   if word in swear_words.keys():
#     replaced_input.append(swear_words[word])
#   else:
#     replaced_input.append(word)
# print replaced_input

# CYPER CHALLENGE

encryption_key = {'a': 'q', 'e': 'z', 'q': 'a', 'z': 'e', 't': 'm', 'm': 't', 'w': 'n', 'n': 'w', 'o': 'r', 'r': 'o',
                  'l': 's', 's': 'l'}
message = "Nobody will ever guess what I'm saying"
message = message.lower()
encoded_message = []

for letter in message:
    if letter in encryption_key.keys():
        encoded_message.append(encryption_key[letter])
    else:
        encoded_message.append(letter)

encoded_message = ','.join(encoded_message).replace(',', '')
print
encoded_message

# Enumerating names

# names = ["Andrew", "Francis", "Precious"]
# for i, person in enumerate(names):
#   print("{}=>{}".format(i,person))