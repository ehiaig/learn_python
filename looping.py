"""
Having the following input

in: "hd..h...d..h.d...h.h"
where h = human and d = dog
We want to move each dog right after the human to give us the output below

output out: "hd..hd.....hd....h.h"

"""
text = "hd..h...d..h.d...h.h"
i = 0
lasth = 0
b = len(text)
while i < b:
    if (text[i]=="d") and (text[i-1] != "h"):
        text=text[:lasth+1] + text[i] + text[lasth + 1:i] + text[i + 1:len(text)]
    elif (text[i]=="h"):
        lasth = i
    i += 1
print (text)