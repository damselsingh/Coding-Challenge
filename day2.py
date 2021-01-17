# fizz buzz game

def fizz_buzz():
    num = int(input('enter a number'))
    if num%3==0 and num%5!=0:
        return "fizz"
    elif num%5==0 and num%3!=0:
        return "Buzz"
    elif num%3==0 and num%5==0:
        return "FizzBuzz"
    else:
        return num

ret=fizz_buzz()
print(ret)