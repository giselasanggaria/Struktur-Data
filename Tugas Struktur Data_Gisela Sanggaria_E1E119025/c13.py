def myReverse(data):
    # returning a new reversed list
    return [data[i] for i in range(len(data)-1, -1, -1)]

print(myReverse([1, 3, 5, 7, 9, 11, 13]))
