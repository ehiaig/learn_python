#Generate numbers 2 to 14 in ascending order
i = 2
while i<=14:
    print(i)
    i = i+3

#Generate the numbers 14 to 2 in a descending order
i = 14
while i>=2:
    print (i)
    i=i-3

#Generate the numbers whether they are even or odd

i = 14
while i>=-1:
    if i>0:
        if i % 2==0:
            print("{} is even".format(i)) #This function converts string to int and vice versa
        else:
            print("{} is odd".format(i))

    else:
        print("{} is negative". format(i))
    i = i - 3


i=0
nums = range(10)
while i<len(nums):
    print(nums[i])
    i+=1

