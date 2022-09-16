
from os import truncate


with open("quotes.txt", "r+", encoding="utf-8") as file:
    
    lines = file.readlines()
    for j, i in enumerate(lines):
        if i != "\n":
            lines[j] = i[:-2]
    
    print ("".join(lines))
    file.seek(0)
    file.truncate(0)
    file.write("".join(lines))
    
        
