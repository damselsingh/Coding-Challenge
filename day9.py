# how do you find the largest and the smallest number in an unsorted integer array

array=[23,779,65,1,90,666]
max = array[0]
min = array[0]
for x in range(len(array)):
    if max<array[x]:
        max=array[x]
    if min>array[x]:
        min=array[x]

print("largest number = ", max)
print("smallest number = ", min)