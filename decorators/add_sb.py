def d1(func):
    def wrap(func1):
        def wrapper(*args):
            print("start code")
            func(*args)
            func1(*args)
            print("end code")
        return wrapper
    return wrap

def add(a,b):
    print("sum is :",a+b)

@d1(add)
def sub(a,b):
    print("sub is:",a-b)
sub(20,10)
