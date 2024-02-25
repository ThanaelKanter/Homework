x=2023
def leap_year(x):
    if x % 4 ==0: return(True)
    if x % 4 > 0: return(False)
print(leap_year(x))