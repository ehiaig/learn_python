#Generate a muliplication table from 1 to 10
"""
for i in range(1,11):
    for j in range(1,11):
        print("{}*{} ={}".format(i,j,(i*j)))

"""

#create the christmas tree below, You have to run this code using the terminal
"""
  *
 ***
*****
"""
for row in range(3):
    for space in range(2-row):
        print(" "),

    for star in range (1+(row*2)):
        print("*"),

    print("\n")

#We can also create the christmas tree with the code below
for i in range(2,1,-1):
    for j in range(1,6,2):
        print(" "*i, "*"*j, " "*i, "\n")
        j += 3
        i-=1

#OR
for line in range(1,4):
    #print("line {}".format(line))
    for space in range(3-line):
        print(" ", end="")
    for stars in range(2*line-1):
        print("*", end="")
    print("")


