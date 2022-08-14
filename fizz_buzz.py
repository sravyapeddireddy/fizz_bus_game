for i in range(100):
    if((i%3!=0)&(i%5!=0)):
        print(i)
    if((i%3==0)&(i%5==0)):
        print(str(i),"fizz buzz")
    else:
        if(i%3==0):
            print(str(i),"fizz")
        if(i%5==0):
            print(str(i),"buzz")

