# how do you count the occurence of a given character i a string
full_name="Riya singh"

for x in range(len(full_name)):
    count=0
    for y in range(x+1, len(full_name)):
        if full_name[x]==full_name[y]:
            count+=1
    

