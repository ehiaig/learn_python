"""
List Examples
"""
nums = [1,2,3,4,5,6]
print(nums[1:6:2])
print(nums[::2]) #This print
print(nums[::-1]) #This reverses and prints index of nums in descending order
print(nums[5:0:-1])
print(nums[-2]) #This prints the second to last element
print(nums[5:]) #This rints eleemtne from the 5th index

#To be sure of the index of each number in the nums list, use  "index()" like below
print(nums.index(2))








