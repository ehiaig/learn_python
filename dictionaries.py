user = {'username':'andrew', 'beauty_level':'high'}
#OR
user = dict(username='andrew', beauty_level = 'high')

#Accessing values with key
print(user['beauty_level'])

#changing values
user['beauty_level']='low'
print(user)

people_named_andrew = {'andrew':'Nudi', 'andrew':'james'}
print(people_named_andrew['andrew'])

#Iterating over dictionary
user.items()#returns an iterator that emits key and value

for key, value in user.items():
    print('key is {}, value is {}'.format(key, value))

#To iterate over all our keys
user.keys()#returns an iterator that emits keys

for key in user.keys():
    print('key is {}'.format(key))

##returns an iterator that emits values
for value in user.values():
    print('value is {}'.format(value))

#What if key doesn't exist?
fruits = {"apple":"red", "orange":"orange", "plum":"purple"}
if "kumquat" in fruits.keys():
    print(fruits['kumquat'])
else:
    print('No kumquat')


"""
Exercise 1:
its the year 2040. Jacon Zuma has taken over the world and declare the follwoing words swear words:
the, and, cow, barn
We are tasked with writing censoring software for the world 
Input: The dogs and cows were at the barn
Output: t-word dogs a-word c-word were at t-word b-word 
"""
swearwords = {'the':'t-word', 'and':'a-word', 'cow':'c-word', 'barn':'b-word'}
text = "The dogs and cows were at the barn"
text = text.lower()
split_text = text.split(' ')
new_words = ""
#print(new_words)
for word in split_text:
    if word in swearwords:
        split_text [split_text.index(word)] = swearwords[word]
        new_words = " ".join(split_text)
print(new_words)

#OR
sentence = "The dogs and cows were at the barn"
sentence = sentence.lower().split()
swear_words = {'the':'t-word', 'and':'a-word', 'cow': 'c-word', 'barn': 'b-word'}
replaced_input = []

for word in sentence:
    if word in swear_words.keys():
        replaced_input.append(swear_words[word])
    else:
        replaced_input.append(word)
print(" ".join(replaced_input))

"""
Exercise 2: Cypher
We need to send messages to the resistance using top secret encryption technology.
We will be changing the following characters so spies cannot read our messages:

A -> Q
E -> Z
Q -> A
Z -> E
T -> M

M -> T
W -> N
N -> W
O -> R
R -> O

L -> S
S -> L

input: "Nobody will ever guess what I'm saying"
output: “wrbrdy niss zvzo guzll nhqm i't lqyiwg”
"""

alphabets = {'a':'q', 'e':'z', 'q':'a', 'z':'e', 't':'m', 'm':'t',
             'w':'n', 'n':'w', 'o':'r', 'r':'o', 'l':'s', 's':'l'}
mytext = "nobody will ever guess what I'm saying"
mytext_list = list(mytext)
new_text = []
for alph in mytext_list:
    if alph in alphabets.keys():
        new_text.append(alphabets[alph])
    else:
        new_text.append(alph)
new_text = ','.join(new_text).replace(',','')
print(new_text)


#OR
encryption_key ={'a':'q', 'e':'z', 'q':'a', 'z':'e','t':'m', 'm':'t', 'w':'n', 'n':'w', 'o':'r', 'r':'o', 'l':'s', 's':'l'}
message = "Nobody will ever guess what I'm saying"
message = message.lower()
encoded_message = []

for letter in message:
  if letter in encryption_key.keys():
    encoded_message.append(encryption_key[letter])
  else:
    encoded_message.append(letter)

encoded_message = ','.join(encoded_message).replace(',', '')
print (encoded_message)

"""
Given a string of text, print the words in the text with the number of 
occurences of each words. i.e if, 'and' occurs 3 times in the sentence, 
print "and' :3

text = "dogs come and eat and eat and eat"
Expected output: {'come':1, 'eat':3, 'dogs':1, 'and':3 }

Algorithm of the Solution:
- convert the text to a list.
- Creating an empty dictionary
- loop through the list
    - For each loop:
        - check for the occurence of the text in the dictionary keys. 
            - if it exist, increment the value
            - if not, add the word to the dictionary and assign it a key of 1
- Print the dictionary
"""

text = "The new quick brown fox jumps over the lazy dog"
text = text.lower().split()
dictionary = {}

for word in text:
    if word in dictionary.keys():
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print(dictionary)

"""
Given a string with a hidden word, write a program that reveals the hidden word.
text = "QPVWQOVWQLVWQIVWQCVWQEV"
Hint: The hidden word is POLICE

Algrithm: 
- Convert the text into a list
- Loop through the given text
    - Take the first value of hidden text, and compare it with the letters in given text
        - if the value of the hidden word is in text
            print the hidden word
        - else, continue looping through the text
"""
text = "QPVWQOVWQLVWQIVWQCVWQEV"
# for character in character array
# if character has an index which starts at 1 and increments by 4
# add the character to the secret message

character_array = list(text)

secret_indices = range(1,len(text),4)
secret_message=[]

for character in character_array:
  for index in secret_indices:
    if character_array.index(character) == index:
      secret_message.append(character)

secret_message = ''.join(secret_message)
print (secret_message)
