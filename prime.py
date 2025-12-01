def prime():
    x=11
    for i in range(2,int(x/2)):
        if(x%i==0):
            print("not prime")
            return
            break;

    print("prime")

prime()
    


