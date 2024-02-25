x = 123456789
def rotate_digits(x):
    z = str(x % 10)
    y = str(x // 10)
    return (z+y)
print(rotate_digits(x))