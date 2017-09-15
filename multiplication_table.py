"""
Create a multiplication table 1-10
"""

for i in range(1,11):
    for j in range(1,11):
        print("{}*{} ={}".format(i,j,(i*j)))

# MULTIPLICATION TABLE (ALTERNATE SOLUTION)

for i in range(1,11):
     print("Multiplication Table for " + str(i) + "'s")
     for j in range(1,11):
         product = str(i*j)
         print(str(i) + " * " + str(j) + " = " + product)


for i in range(1,13):
    print("####################### NEXT NEXT NEXT #############################")
    for j in range(1,13):
        ans=i*j
        print(str(i) + " * " +  str(j) + " = " + str(ans))


