def conj(nombreComplexe):
    if "+" in nombreComplexe:
        return nombreComplexe.replace("+", "-")
    else:
        return nombreComplexe.replace("-", "+")