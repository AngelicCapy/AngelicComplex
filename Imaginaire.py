def Im(nombreComplexe):
    if nombreComplexe[0] == "-":
        nombreComplexe = nombreComplexe[1:]
        
    if "+" in nombreComplexe:
        nombreComplexe = nombreComplexe.split("+")
        return nombreComplexe[1]
    else:
        nombreComplexe = nombreComplexe.split("-")
        return "-" + nombreComplexe[1]
