# write a function for checking the speed of drivers. the function should have one parameter : speed
# 1. if speed is less than 70, it should print "OK"
# 2. otherwise, for every 5km above the speed limit(70), it should give the driver one demerit points. For example,
# if  the speed is 80, it should print. "Point: 2".
# 3. If the driver gets more than 12 points, the function should print: "License suspended"

def driver(speed=10):
    if speed <= 70:
        return "OK"
    if speed > 70:
        total = (speed-70)/5
        if total >=12:
            return "License suspended"
        else:
            return ("Points ", int(total))



lim = driver(int(60))
print(lim)


