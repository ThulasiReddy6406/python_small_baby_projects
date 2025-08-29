''' text formatting using "capitalize" -- "title"--"low/upp"--'''

para = input("ENTER A SENTENCE OR PARAGRAPH :-  ")
para_split = para.split()

cap = " ".join(para_split)
cappi = cap.capitalize()
title = cap.title()
low = cap.lower()
upp = cap.upper()
print(cappi)
print(title,low,upp)