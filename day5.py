# write a function called show_stars(rows). if rows is 5, it should print the following
def show_stars(row=5):
    for x in range(row+1):
        for y in range(x):
            print('*', end='')
        print()

    


show_stars()