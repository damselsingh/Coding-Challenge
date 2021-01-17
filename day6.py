# write a function that prints all the prime number between 0 to limit where limit is a parameter
# //- floor division

def prime():
    for num in range(1, 101):
        count=0
        for i in range(2, num//2+1):   
            if(num%i==0):
                count+=1
                break
        if (count == 0 and num!=1):
            print(num, end=' ')


prime()