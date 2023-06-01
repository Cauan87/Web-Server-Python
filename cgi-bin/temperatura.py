#!/usr/bin/env python3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')
result_final: str

def analyzing_value(value):
    if value:
        return int(value)
    else:
        return -1

def same_units(value, unity):
        if unity == 'cel':
            return f'Unidades iguais => {value:.2f} Celsius'
        elif unity == 'kel':
            return f'Unidade iguais => {value:.2f} Kelvin'
        else:
            return f'Unidade iguais => {value:.2f} Fahrenheit'
def convert_from_fah(value, unity):
    if unity == 'cel':
        return f'{value} Graus Fahrenheit = {((value - 32) / 1.8):.2f} Kelvin'
    elif unity == 'kel':
        return f'{value} Graus Fahrenheit = {((value - 32) / 1.8):.2f} Graus Celsius'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_from_kel(value, unity):
    if unity == 'cel':
        return f'{value} Kelvin = {(value - 273.15):.2f} Graus Celsius'
    elif unity == 'fah':
        return f'{value} Kelvin = {(((value - 273.15) * 1.8) + 32):.2f} Graus Fahrenheit'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_from_cel(value, unity):
    if unity == 'kel':
        return f'{value} Graus Celsius = {(value + 273.15):.2f}  Kelvin'
    elif unity == 'fah':
        return f'{value} Graus Celsius = {((1.8 * value) + 32):.2f} Graus Fahrenheit'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_units(value, unity1, unity2):
    if value != -1 and value != 'typeError':
        if unity1 == unity2 and unity1 != 'sel':
            return same_units(value, unity1)
        elif unity1 != 'sel' and unity2 =='sel':
            result = 'Erro: Selecione uma unidade !'

        elif unity1 == 'cel':
           return convert_from_cel(value, unity2)
        elif unity1 == 'fah':
            return convert_from_fah(value, unity2)
        elif unity1 == 'kel':
            return convert_from_kel(value, unity2)
        else:
            result = 'Erro: Selecione uma unidade !'
    elif value == 'typeError':
        result = 'Erro: Tipo de Valor inesperado !'
    else:
        result = 'Erro: Campos sem valores !'

try:
    value = analyzing_value(received)

except:
    value = 'typeError'

try:
    result_final = convert_units(value, unity1, unity2)

except:
    result_final = 'Erro Inesperado'

print("Content-Type: text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('<title>Resultado: Temperatura</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print("<h2>{}</h2>".format(result_final))
print('<a class="back" href="../temperatura.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")

