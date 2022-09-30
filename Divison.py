from Conjurer import *
from Multiplication import *
def cdiv(nombreComplexeA, nombreComplexeB):

    a = cmul(nombreComplexeA, conj(nombreComplexeB))
    b = cmul(nombreComplexeB, conj(nombreComplexeB))
    return str(a)+"/"+str(b)[:-3]
    