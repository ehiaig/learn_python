"""
Excercise 1:
Print Andrew is beautiful
"""
name = "Andrew"
IS_BEAUTIFUL = True
if (name == "Andrew") and (IS_BEAUTIFUL):
    print("Oh, hello Beautiful")

"""
Excercise 2:
Loop through the numbers 15-68. If number is even or divisible by 3,
print "this number is even and divisible by 3"
"""
for num in range(15, 69):
    if (num%2==0) and (num%3==0):
        print("{} is even and divisible by 3".format(num))

#Calling functions
def complem(message, name="Andrew"):
    print("{} is {}".format(name, message))
complem("Andrew", "exhausted")
complem(message="exhausted", name="Andrew")
me = "Andrew"
what_to_say= "exhausted"
complem(me, what_to_say)