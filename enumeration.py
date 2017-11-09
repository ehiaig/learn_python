#enumerate iterates over a list, not really a dictuonary.
# It prints out the index of objects in a list.
# It unpacks the value of a dictionary and prints the index and key, not the values in the dictionary

nums = {'1':'Ehi', '2':'Ayo'}
num1=['a', 'b', 'c']

for index, val in enumerate(num1):
    print(index, val)
print('*********')
for objs in enumerate(num1):
    print(objs)
print('*********')
for objs in enumerate(nums):
    print(objs)