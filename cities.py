with open("cities.txt","r") as a:
    b=a.read()
    print(b)
    print(type(b))
    c=b.split("\n")
    print(c)
    i=0
    while i<len(c):
        if "delhi" in c[i]:
            with open("delhi.txt","a") as d:
                d.write(c[i])
                d.write("\n")
        elif "shimla" in c[i]:
            with open("shimla.txt","a") as e:
                e.write(c[i])
                e.write("\n")
        
        else:
            with open("otherwise.txt","a") as f:
                f.write(c[i])
                f.write("\n")
        i=i+1
        