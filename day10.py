# how do you find all the pairs of an integer array whose sum is equal to an given number

arr=[2,9,5,8,6,4,3,1]
sum=10
for x in range(len(arr)):
    for y in range(x+1, len(arr)):
        if (arr[x]+arr[y]==sum):
            print(arr[x], "+", arr[y], "=", sum)