def d1(func):
    def wrapper(*args, **kwargs):
        name=input("enter your name: ")
        age=input("enter your age: ")
        print("prosseeing your details")

        return func(name,age)
        
    return wrapper
@d1
def emp(name,age):
    print("name:", name)
    print("age:", age)

emp()
