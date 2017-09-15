"""
Exercise 1: Print all prime numbers from 1 - 200
"""
for num in range(1,200):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print ("{} is prime".format(num))

"""
Exercise 2: Print every other number in the list 1 to 6. 
Solution: This means we're printing 2,4,6 
"""
nums =[1,2,3,4,5,6]
for num in range(1,len(nums),2):
    print (nums[num])


"""
Exercise 3: Print and Count the number of times an item appears in a list below
"""
mylist = ["Hi", 3, 5, 2, "Ho", "Hi"]
print(mylist.count("Ho"))