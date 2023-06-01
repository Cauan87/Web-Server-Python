#!/usr/bin/env python3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')
result_final = None

def analyzing_value(value):
    if value:
        return int(value)
    else:
        return -1

def same_units(value, unity):
        if unity == 'kg':
            return f'Unidades iguais => {value:.2f} Quilogramas'
        elif unity == 'gr':
            return f'Unidade iguais => {value:.2f} Gramas'
        else:
            return f'Unidade iguais => {value:.2f} Miligramas'

def convert_from_kg(value, unity):
    if unity == 'gr':
        return f'{value} Quilogramas = {(value * 1000):.2f} Gramas'
    elif unity == 'mg':
        return f'{value} Quilogramas = {(value * 1000000):.2f} Miligramas'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_from_gr(value, unity):
    if unity == 'kg':
        return f'{value} Gramas = {(value / 1000):.2f} Quilogramas'
    elif unity == 'mg':
        return f'{value} Gramas = {(value * 1000):.2f} Miligramas'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_from_mg(value, unity):
    if unity == 'kg':
        return f'{value} Miligramas = {(value / 1000000):.2f} Quilogramas'
    elif unity == 'gr':
        return f'{value} Miligramas = {(value / 1000):.2f} Gramas'
    else:
        return 'Erro: Selecione uma unidade!'

def convert_units(value, unity1, unity2): 
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