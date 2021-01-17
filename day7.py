# How do you find the missing number in a given integer array of 1 to n

num = [1,3,4,5,6,7,8,9,10]
count=1
for x in range(len(num)):
    if count!=num[x]:
        print(count, " is missing")
        count = num[x]
    count+=1