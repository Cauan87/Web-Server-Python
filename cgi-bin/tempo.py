#!/usr/bin/env python3

import cgitb, cgi

cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')

def analyzing_value(value):
    if value:
        return int(value)
    else:
        return -1

try:
    value = analyzing_value(received)

except:
    value = 'typeError'

def convert_units(value, unity1, unity2):
    if value != -1 and value != 'typeError':
        if unity1 == unity2 and unity1 != 'sel':
            if unity1 == 'seg':
                result = f'Unidades iguais => {value:.2f} Segundos'
                
            elif unity1 == 'min':
                result = f'Unidade iguais => {value:.2f} Minutos'

            else:
                result = f'Unidade iguais => {value:.2f} Horas'
        elif unity1 != 'sel' and unity2 =='sel':
            result = 'Erro: Selecione uma unidade !'

        elif unity1 == 'seg':
            if unity2 == 'min':
                result = f'{value} Segundos = {(value / 60):.2f} Minutos'

            elif unity2 == 'hr':
                result = f'{value} Segundos = {(value / 3600):.2f} Horas'
        elif unity1 == 'min':
            if unity2 == 'seg':
                result = f'{value} Minutos = {(value * 60):.2f} Segundos'

            elif unity2 == 'hr':
                result = f'{value} Minutos = {(value / 60):.2f} Horas'

        elif unity1 == 'hr':
            if unity2 == 'seg':
                result = f'{value} Horas = {(value * 3600):.2f} Segundos'

            elif unity2 == 'min':
                result = f'{value} Horas = {(value * 60):.2f} Minutos'

        else:
            result = 'Erro: Selecione uma unidade !'

    elif value == 'typeError':
        result = 'Erro: Tipo de Valor inesperado !'

    else:
        result = 'Erro: Campos sem Valores !'

    return result

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

