# how do you print duplicate characters from a string
name="riya singha"

for x in range(len(name)):
    for y in range(x+1, len(name)):
        if name[x]==name[y]:
            print(name[x], " has duplicate")


