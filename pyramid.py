"""
Exercise 1: Create a pyramid like below
    *
   ***
  *****
   ***
    *
"""
for line in [1,2,3,2,1]:
     #print("line {}".format(line))
    for space in range(3-line):
        print(" ", end="")

    for stars in range(2*line-1):
        print("*", end="")
    print("")
#OR

line = 1
counter = 1
while line>0:
    if line==3:
        counter = -1
#    print(line)
    for space in range(3 - line):
        print(" ", end="")

    for stars in range(2 * line - 1):
        print("*", end="")
    print("")
    line += counter

#and a larger pyramid
line = 1
counter = 1
while line>0:
    if line==5:
        counter = -1
#    print(line)
    for space in range(5 - line):
        print(" ", end="")

    for stars in range(2 * line - 1):
        print("*", end="")
    print("")
    line += counter
