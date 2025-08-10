arr =[]
def square(number):
    if 1<= number <=64:
        number = number-1
        total = 2**number
        arr.append(total)
        return total
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    for x in arr:
        x+=x
    return x-1
