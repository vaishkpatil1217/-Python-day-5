import time

def d1(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution = end - start
        print(f"Function period took ",execution," seconds to execute")
        return result
    return wrapper

@d1
def period(a,b):
    return a+b,a-b

result=period(20,5)
print(result)
