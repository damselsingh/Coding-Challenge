# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit(parameter).
# for example, if limit is 20, it should return the sum of 3,5,6,9,10,12,15,18,20.



def func(limit=20):
    count=0
    for x in range(1,limit+1):
        if x%3==0 or x%5==0:
            count=count+x
    print(count)

func()
