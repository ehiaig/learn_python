"""
curtains.py
Problem: Calculate how much material to buy, given the size of the windows.
Target Users: My friend who wants to make some curtains
Target System: GNU/Linux
Interface: Command-line
Functional Requirements: Print out the required length of fabric in meters
Print out the total price of the fabric
User must be able to input the measurements of the window
Testing: Simple run test
Maintainer: maintainer@website.com
"""

# To start with, all the measurements will be in cm
# Assume that the roll of material is going to be 140cm wide
# and that the price per meter will be 5 units of currency
rollwidth = 140
pricepermetre = 5
# Prompt the user to input the window measurements in cm
windowheight = input('Enter the height of the window (cm): ')
windowwidth = input('Enter the width of the window (cm): ')
# Add a bit for the hems
# First we must convert the string into a number
# otherwise we will get an error if we try to perform arithmetic on a text string
curtainwidth = float(windowwidth) * 0.75 + 20
curtainlength = float(windowheight) + 15
# Work out how many widths of cloth will be needed
# and figure out the total length of material for each curtain (in cm still)
widths = curtainwidth / rollwidth
totallength = curtainlength * widths
# Actually there are two curtains, so we must double the amount of material
# and then divide by 10 to get the number of meters
totallength = (totallength * 2) / 10
# Finally, work out how much it will cost
price = totallength * pricepermetre
# And print out the result
print("You need", totallength, "meters of cloth for ", price)

# print headers for the basic trace table
print()
print('\twidth\theight\twidths\ttotal\tprice')
# I need to add a bit for the hems.
# First, I must convert the string into a number.
# Otherwise, I will get an error if I try to perform arithmetic on a text string.
curtainwidth = (float(windowwidth) * 0.75) + 20

print('\t', curtainwidth)
curtainlength = float(windowheight) + 15
print('\t\t', curtainlength)
# Now, I need to work out how many widths of cloth will be needed
# and figure out the total length of material for each curtain (in cm still).
widths = curtainwidth / rollwidth
print('\t\t\t', widths)
totallength = curtainlength * widths
print('\t\t\t\t', totallength)
# Actually, I have two curtains, so I must double the amount of material
# and then divide by 10 to get the number of meters.
totallength = (totallength * 2) / 10
print('\t\t\t\t', totallength)
# Finally, I need to work out how much it will cost.
price = totallength * pricepermetre
print('\t\t\t\t\t', price)