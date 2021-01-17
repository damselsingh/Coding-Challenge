# Write a function called showNumbers that takes a parameter called limit. it should print all the numbers
# between 0 and limit with a label to identify the evn and odd numbers. For example, if the limit is 3, it should
# print: 0 EVEN, 1 ODD, 2 EVEN, 3 ODD

def showNumbers(limit=3):
    for x in range(limit):
        if x%2==0:
            print(x, "EVEN")
        else:
            print(x, "ODD")

showNumbers(int(5))