def cdif(nombreComplexeA,nombreComplexeB):
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

    a = int(nombreA[0]) - int(nombreB[0])
    b = int(nombreA[1][:-1]) + int(nombreB[1][:-1])

    if b < 0:
        return str(a)+str(b)+"i"
    else:
        return str(a)+"+"+str(b)+"i"