def cmul(nombreComplexeA, nombreComplexeB):
    if "+" in nombreComplexeA:
        nombreA = nombreComplexeA.split("+")
    else:
        nombreA = nombreComplexeA.split("-")
        nombreA[1] = "-"+nombreA[1]
    
    if "+" in nombreComplexeB:
        nombreB = nombreComplexeB.split("+")

    else:
        nombreB = nombreComplexeB.split("-")
        nombreB[1] = "-"+nombreB[1]
    
    a = int(nombreA[0]) * int(nombreB[0])
    b = int(nombreA[0]) * int(nombreB[1][:-1])
    c = int(nombreA[1][:-1]) * int(nombreB[0])
    d = (int(nombreA[1][:-1]) * int(nombreB[1][:-1])) * -1
    
    return str(a+d)+"+"+str(b+c)+"i"