# how do you find the duplicate number on a given integer array

array = [1,2,4,1,6,8,4,9,0,2]
for x in range(len(array)):
    for y in range(x+1, len(array)):
        if array[x]==array[y]:
            print(array[x], " has duplicate")