
def Recur_facto(n, a=1):
    if (n == 0):
        return a

    return Recur_facto(n - 1, n * a)



print(Recur_facto(6))
