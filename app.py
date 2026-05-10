from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/reglas', methods=['GET', 'POST'])
def reglas():

    mensaje = ""
    desbloqueado = False

    if request.method == 'POST':

        respuesta1 = request.form['respuesta1']
        respuesta2 = request.form['respuesta2']
        respuesta3 = request.form['respuesta3']
        respuesta4 = request.form['respuesta4']
        respuesta5 = request.form['respuesta5']

        if respuesta1 == "3":
            mensaje += "Respuesta 1: Correcta <br>"
        else:
            mensaje += "Respuesta 1: Incorrecta <br>"

        if respuesta2 == "10":
            mensaje += "Respuesta 2: Correcta <br>"
        else:
            mensaje += "Respuesta 2: Incorrecta <br>"

        if respuesta3 == "0":
            mensaje += "Respuesta 3: Correcta <br>"
        else:
            mensaje += "Respuesta 3: Incorrecta <br>"

        if respuesta4 == "1":
            mensaje += "Respuesta 4: Correcta <br>"
        else:
            mensaje += "Respuesta 4: Incorrecta <br>"

        if respuesta5 == "1":
            mensaje += "Respuesta 5: Correcta <br>"
        else:
            mensaje += "Respuesta 5: Incorrecta <br>"

        correctas = 0

        if respuesta1 == "1":
            correctas += 1
        if respuesta2 == "10":
            correctas += 1
        if respuesta3 == "0":
            correctas += 1
        if respuesta4 == "1":
            correctas += 1
        if respuesta5 == "1":
            correctas += 1

        if correctas >= 2 and 'compromiso' in request.form:
            desbloqueado = True

    return render_template(
        'reglas.html',
        mensaje=mensaje,
        desbloqueado=desbloqueado
    )

@app.route('/notas', methods=['GET', 'POST'])
def notas():
    mensaje = ""
    desbloqueado = False

    if request.method == 'POST':

        respuesta1 = request.form['respuesta1']
        respuesta2 = request.form['respuesta2']
        respuesta3 = request.form['respuesta3']

        if respuesta1 == "40":
            mensaje += "Respuesta 1: Correcta <br>"
        else:
            mensaje += "Respuesta 1: Incorrecta <br>"

        if respuesta2 == "40":
            mensaje += "Respuesta 2: Correcta <br>"
        else:
            mensaje += "Respuesta 2: Incorrecta <br>"

        if respuesta3 == "50":
            mensaje += "Respuesta 3: Correcta <br>"
        else:
            mensaje += "Respuesta 3: Incorrecta <br>"

        correctas = 0

        if respuesta1 == "40":
            correctas += 1
        if respuesta2 == "40":
            correctas += 1
        if respuesta3 == "50":
            correctas += 1

        if correctas >= 2 and 'compromiso' in request.form:
            desbloqueado = True

    return render_template(
        'notas.html',
        mensaje=mensaje,
        desbloqueado=desbloqueado
    )

@app.route('/skills', methods=['GET', 'POST'])
def skills():
    mensaje = ""
    desbloqueado = False

    if request.method == 'POST':

        respuesta1 = request.form['respuesta1']
        respuesta2 = request.form['respuesta2']

        if respuesta1 == "1":
            mensaje += "Respuesta 1: Correcta <br>"
        else:
            mensaje += "Respuesta 1: Incorrecta <br>"

        if respuesta2 == "4":
            mensaje += "Respuesta 2: Correcta <br>"
        else:
            mensaje += "Respuesta 2: Incorrecta <br>"

        correctas = 0

        if respuesta1 == "1":
            correctas += 1
        if respuesta2 == "4":
            correctas += 1

        if correctas >= 2 and 'compromiso' in request.form:
            desbloqueado = True

    return render_template(
        'skills.html',
        mensaje=mensaje,
        desbloqueado=desbloqueado
    )

@app.route('/fechas', methods=['GET', 'POST'])
def fechas():
    mensaje = ""
    desbloqueado = False

    if request.method == 'POST':

        respuesta1 = request.form['respuesta1']
        respuesta2 = request.form['respuesta2']
        respuesta3 = request.form['respuesta3']

        if respuesta1 == "1":
            mensaje += "Respuesta 1: Correcta <br>"
        else:
            mensaje += "Respuesta 1: Incorrecta <br>"

        if respuesta2 == "2":
            mensaje += "Respuesta 2: Correcta <br>"
        else:
            mensaje += "Respuesta 2: Incorrecta <br>"

        if respuesta3 == "3":
            mensaje += "Respuesta 3: Correcta <br>"
        else:
            mensaje += "Respuesta 3: Incorrecta <br>"

        correctas = 0

        if respuesta1 == "1":
            correctas += 1
        if respuesta2 == "2":
            correctas += 1
        if respuesta3 == "3":
            correctas += 1

        if correctas >= 2 and 'compromiso' in request.form:
            desbloqueado = True

    return render_template(
        'fechas.html',
        mensaje=mensaje,
        desbloqueado=desbloqueado
    )

if __name__ == '__main__':
    app.run(debug=True)