def max(list):
    if(len(list)== 1):
        return list [0]
    else:
        maxVal = max(list [1:])
    if(maxVal < list[0]):
        maxVal = list[0]
    return maxVal
list = [13,6,30,20,20]
maxvalue = max(list)
print(maxvalue)