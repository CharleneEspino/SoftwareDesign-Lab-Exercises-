def power(r, louise):
    if(louise == 0):
        return 1
    else:
        return r * power(r,louise -1)
print(power(3,21))