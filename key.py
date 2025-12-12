def key(**kwarge):
    if kwarge:
        print("--------information--------")
        for key,value in kwarge.items():
            print(key,":",value)
    else:
        print("\n----------no information----------")

key(name="hrishi",age=22,city="mumbai")
key(job="vfx artist",salary=10000)
key(country="india",state="maharastra",pincode=425406)
key()