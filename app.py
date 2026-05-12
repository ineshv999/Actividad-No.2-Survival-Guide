from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/reglas', methods=['GET', 'POST'])
def reglas():

    desbloqueado = False
    correctas = 0

    if request.method == 'POST':

        respuesta1 = request.form['respuesta1']
        respuesta2 = request.form['respuesta2']
        respuesta3 = request.form['respuesta3']
        respuesta4 = request.form['respuesta4']
        respuesta5 = request.form['respuesta5']

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
        desbloqueado=desbloqueado, 
        correctas=correctas
    )

@app.route('/notas', methods=['GET', 'POST'])
def notas():

    desbloqueado = False
    correctas = 0

    if request.method == 'POST':

        respuesta1 = request.form['respuesta1']
        respuesta2 = request.form['respuesta2']
        respuesta3 = request.form['respuesta3']

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
        correctas=correctas,
        desbloqueado=desbloqueado
    )

@app.route('/skills', methods=['GET', 'POST'])
def skills():
    
    correctas = 0
    desbloqueado = False

    if request.method == 'POST':

        respuesta1 = request.form['respuesta1']
        respuesta2 = request.form['respuesta2']

        correctas = 0

        if respuesta1 == "1":
            correctas += 1
        if respuesta2 == "4":
            correctas += 1

        if correctas >= 2 and 'compromiso' in request.form:
            desbloqueado = True

    return render_template(
        'skills.html',
        correctas=correctas,
        desbloqueado=desbloqueado
    )

@app.route('/fechas', methods=['GET', 'POST'])
def fechas():
    desbloqueado = False
    correctas = 0

    if request.method == 'POST':

        respuesta1 = request.form['respuesta1']
        respuesta2 = request.form['respuesta2']
        respuesta3 = request.form['respuesta3']

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
        correctas=correctas,
        desbloqueado=desbloqueado
    )

if __name__ == '__main__':
    app.run(debug=True)