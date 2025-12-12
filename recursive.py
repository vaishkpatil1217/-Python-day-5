def recursive(x):
    if(x!=0):
        return x+recursive(x-1)
    else:
        return 0

print(recursive(5))
