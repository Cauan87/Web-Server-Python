#!/usr/bin/env python3

import cgitb, cgi

cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')

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
    if unity == 'hr':
        return f'Unidades iguais => {value:.2f} Horas'
    elif unity == 'min':
        return f'Unidade iguais => {value:.2f} Minutos'
    else:
        return f'Unidade iguais => {value:.2f} Segundos'

def convert_from_hr(value, unity):
    """
    has its fixed unit "hr" and checks the unit defined in unity,
    then converts from "hr" to unity unit

    Args:
        value: value defined in the html input
        unity: compare selected unit in html and convert based on it

    Returns:
        if value is true: returns the value in hr + the formatted value based
        on the selected unit of unity.
        if value is false: returns error.
    """
    if unity == 'seg':
        return f'{value} Horas = {(value * 3600):.2f} Segundos'
    elif unity == 'min':
        return f'{value} Horas = {(value * 60):.2f} Minutos'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_from_min(value, unity):
    """
    has its fixed unit "min" and checks the unit defined in unity,
    then converts from "min" to unity unit.

    Args:
        value: value defined in the html input.
        unity: compare selected unit in html and convert based on it.

    Returns:
        if value is true: returns the value in min + the formatted value based
        on the selected unit of unity.
        if value is false: returns error.
    """
    if unity == 'seg':
        return f'{value} Minutos = {(value * 60):.2f} Segundos'
    elif unity == 'hr':
        return f'{value} Minutos = {(value / 60):.2f} Horas'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_from_seg(value, unity):
    """
    has its fixed unit "seg" and checks the unit defined in unity,
    then converts from "seg" to unity unit.

    Args:
        value: value defined in the html input.
        unity: compare selected unit in html and convert based on it.

    Returns:
        if value is true: returns the value in seg + the formatted value based
        on the selected unit of unity.
        if value is false: returns error 
    """
    if unity2 == 'min':
        return f'{value} Segundos = {(value / 60):.2f} Minutos'
    elif unity2 == 'hr':
        return f'{value} Segundos = {(value / 3600):.2f} Horas'
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
        elif unity1 != 'sel' and unity2 =='sel':
            result = 'Erro: Selecione uma unidade !'
        elif unity1 == 'hr':
           return convert_from_hr(value, unity2)
        elif unity1 == 'min':
            return convert_from_min(value, unity2)
        elif unity1 == 'seg':
            return convert_from_seg(value, unity2)
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
print('<title>Resultado: Tempo</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print("<h2>{}</h2>".format(result_final))
print('<a class="back" href="../tempo.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")

