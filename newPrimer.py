""" 'Easier' Prime numbers logic"""
def primer(start, end):
    """A method to print prime numbers between a certain range"""
    for i in range(start, end - 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:   # still invetsigating why this code only works when put here
                print(i)


primer(10, 100)
