"""
Write a multiplicaton for 4, 5, 9, 11 running from 1 to 12
ALGORITHM:

- Define a list that contains the numbers to be multiplied (4,5,9,11)
- Define a loop through the number in the range 1-13
- Do the multiplication
- print the format of the output
"""
for i in (4,5,9,11):
    print("**** Next Multiplication ****")
    for j in range(1,13):
        answer = i*j
        print(str(i) + " * "+ str(j) +" = "+str(answer))

#OR
for multiplier in (4, 5, 9, 11):
    print("**** Next Multiplication Table****")
    for number in range(1,13):
        answer = multiplier * number
        print("{} * {} = {}".format(multiplier,number,answer))
