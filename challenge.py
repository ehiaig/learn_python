# print ("input is {}".format(input))
# ALTERNATE HUMAN AN DDOG CHALLENGE
stirr = "hd...h...d..d..hd...h..d..h.d"
stir = list(stirr)
line = 0
while (line < len(stir)):
    try:
        if stir[line] == 'h' and not(stir[line+1] == 'd'):
#       #print (stir[line], stir[line + 1])
            for ch in stir[line + 1:]:
                if ch == 'd':
                    ch, stir[line +1] = stir[line +1], ch
    except (IndexError):
        break
    line = line + 1

print (''.join(stir))

# HUMAN AND DOG CHALLENGE
# Put all dogs one step in from of human
