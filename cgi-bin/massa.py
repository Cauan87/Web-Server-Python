#!/usr/bin/env python3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')
result_final: str

def analyzing_value(value):
    """
    Analyzes the value received in the html input, 
    if it has any value, it is returned as an integer, 
    otherwise, it returns -1

    Args:
        value: received in the input value of the html

    Returns:
        value: value will be returned with integer
        -1: the input was empty

    """
    if value:
        return int(value)
    else:
        return -1

def same_units(unity):
    """
    Checks if the units defined in the html input are the same

    Args:
        unity: checks if the unit was the same in both selectors
    
    Returns:
        according to the unit, returns a formatted text saying they are equal

    """
    if unity == 'kg':
        return f'Unidades iguais => {value:.2f} Quilogramas'
    elif unity == 'gr':
        return f'Unidade iguais => {value:.2f} Gramas'
    else:
        return f'Unidade iguais => {value:.2f} Miligramas'

def convert_from_kg(value, unity):
    """
    has its fixed unit "kg" and checks the unit defined in unity,
    then converts from "kg" to unity unit.

    Args:
        value: value defined in the html input.
        unity: compare selected unit in html and convert based on it.

    Returns:
        if value is true: returns the value in kg + the formatted value based
        on the selected unit of unity.
        if value is false: returns error.
    """
    if unity == 'gr':
        return f'{value} Quilogramas = {(value * 1000):.2f} Gramas'
    elif unity == 'mg':
        return f'{value} Quilogramas = {(value * 1000000):.2f} Miligramas'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_from_gr(value, unity):
    """
    has its fixed unit "gr" and checks the unit defined in unity,
    then converts from "gr" to unity unit.

    Args:
        value: value defined in the html input.
        unity: compare selected unit in html and convert based on it.

    Returns:
        if value is true: returns the value in gr + the formatted value based
        on the selected unit of unity.
        if value is false: returns error.
    """
    if unity == 'kg':
        return f'{value} Gramas = {(value / 1000):.2f} Quilogramas'
    elif unity == 'mg':
        return f'{value} Gramas = {(value * 1000):.2f} Miligramas'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_from_mg(value, unity):
    """
    has its fixed unit "mg" and checks the unit defined in unity,
    then converts from "mg" to unity unit.

    Args:
        value: value defined in the html input.
        unity: compare selected unit in html and convert based on it.

    Returns:
        if value is true: returns the value in mg + the formatted value based
        on the selected unit of unity.
        if value is false: returns error.
    """
    if unity == 'kg':
        return f'{value} Miligramas = {(value / 1000000):.2f} Quilogramas'
    elif unity == 'gr':
        return f'{value} Miligramas = {(value / 1000):.2f} Gramas'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_units(value, unity1, unity2):
    """
    Checks if value is different from -1 and different from 
    "TypeError" (defined in try and except), if value is true,
    it will make a series of comparisons, including if unity1 and unity2 
    receive the same value, in which case they return the same_units function .

    In other cases it will check the unit of unity, 
    and based on that it will call the convert_from_"chosen unit" function.

    Ultimately, if it doesn't fit any of the other comparisons, 
    it assumes that no box has been selected.

    Args:
        value: uses value to check if it is different from -1 and different from "typeError".
        unity1: compare selected unit in html and convert by calling corresponding function.

    Returns:
        if the value is different from -1 and different from "typeError",
        the function continues, otherwise, if it fits in "TypeError" 
        it returns an error message, in the last case, it returns "Error, field is empty".
    """ 
    if value != -1 and value != 'typeError':
        if unity1 == unity2 and unity1 != 'sel':
            return same_units(value, unity1)
        elif unity1 != 'sel' and unity2 == 'sel':
            return 'Erro: Selecione uma unidade!'
        elif unity1 == 'kg':
            return convert_from_kg(value, unity2)
        elif unity1 == 'gr':
            return convert_from_gr(value, unity2)
        elif unity1 == 'mg':
            return convert_from_mg(value, unity2)
        else:
            return 'Erro: Selecione uma unidade!'
    elif value == 'typeError':
        return 'Erro: Tipo de Valor inesperado!'
    else:
        return 'Erro: Campos sem valores!'

try:
    """
    tries to see if any value has been set.
    """
    value = analyzing_value(received)
except:
    """
    sets value to 'typeError'.
    """
    value = 'typeError'

try:
    """
    try to convert the units of the function and store them in the result_final variable. 
    """
    result_final = convert_units(value, unity1, unity2)
except:
    """
    sets result_final to 'Erro Inesperado'.
    """
    result_final = 'Erro Inesperado'

print("Content-Type: text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('<title>Resultado: Massa</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print("<h2>{}</h2>".format(result_final))
print('<a class="back" href="../massa.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")