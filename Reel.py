def Re(nombreComplexe):
    if nombreComplexe[0] == "-":
        nombreComplexe = nombreComplexe[1:]
        if "+" in nombreComplexe:
            nombreComplexe = nombreComplexe.split("+")
            return nombreComplexe[0]
        
        else:
            nombreComplexe = nombreComplexe.split("-")
            return "-" + nombreComplexe[0]


    else:
        NombreComplexe = nombreComplexe
        if "+" in nombreComplexe:
            nombreComplexe = nombreComplexe.split("+")
            return nombreComplexe[0]
        else:
            nombreComplexe = nombreComplexe.split("-")
            return "-" + nombreComplexe[0]
