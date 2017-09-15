#For loops are for lists and ranges
my_num = [3,5,7,6,100]
for num in my_num:
    print (num+3)

#Another
range(8)

#Yet another
for num in range(5):
    print(num)
#For
for num in range(1,5):
    print(num)

#Again
for num in range(1,10, 2):
    print(num)

#Yet
for i in range(2):
    for j in range(3):
        print("{}*{} ={}".format(i,j,(i*j)))
"""
To get the the documanetation of each function use thes
print(range.__doc__)
OR
print
while loops are for conditions that requires a certain action to be true
and until we create a condition to make it false.
"""