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
Write a function, that accepts a string as an argument, and returns either True or False, whether the string can be made into a palindrome or not.

For example: 
aabb is not a palindrome. However, it can be rearranged to form a palindrome – even two: abba and baab

Algorithm:      

- Break word into list, 
- Count the items in list.
    - If even, break into 2 halfs,
    - Else, get the middle letter, 
- Break the list into 2 halfs. 
- check if the first list is equal to the reverse of the second list
"""

word = str(input("Enter the word to be checked: "))
#word = list(word)

breakword = int(round(len(word)/2.0))
result, b = [word[i:i+breakword] for i in range(0,len(word),breakword)]

rvs_word = b [::-1]
if result==rvs_word:
    print("Yay")

# def palin():
    

