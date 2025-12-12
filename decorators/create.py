def d1(func):
    def wrapper(*args, **kwargs):
        print("your detail")
        func(*args,**kwargs)
        print("thank for using decorators")
        print("---------------------------------------")
    return wrapper


@d1
def student(name,age):
    print("name:",name)
    print("age:",age)

student("rohit",20)

@d1
def emp(name,salary=9000):
    print("name :",name," salry :",salary)
    
emp("hrishi",30000)
emp("hrishi")
