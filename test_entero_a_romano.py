"""
1.Crear una funcion que pase de entero >0 y <4000 a romano
2.Cualquier otra entrada debe dar error

Casos de prueba
a)1194-->MCMXCIV
b)4000->RomanNumberError("El valor debe ser menor de 4000")
c)"unacadena"->RomanNumberError("Debe ser un entero")
d)0->RomanNumberError("El valor debe ser mayor a cero")
e)-3->RomanNumberError("El valor debe ser mayor a cero")
f)4.5->RomanNumberError("Debe ser un entero")
"""

def test_error_si_entero_mayor_de_3999():
    numero entero_a_romano(1994)=="MCMXCIV"



def test_3_es_igual_a_2_mas_uno():     #debe empezar por test la funcion
    assert 2 + 1 == 3                            #siempre tenemos que poner el assert es un mandato para comprobar si la cosa va bien