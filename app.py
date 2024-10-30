from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'unaclavesecreta' 

# Usuario
users = {
    'admin': '54321'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario', methods=['POST'])
def usuario():
    usu = request.form['usu']
    contraseña = request.form['contraseña']

    if usu in users and users[usu] == contraseña:
        session['usu'] = usu
        flash('Inicio de sesión exitoso!')
        return redirect(url_for('bienvenido'))
    else:
        flash('Nombre de usuario o contraseña incorrectos.')
        return redirect(url_for('index'))

@app.route('/bienvenido')
def bienvenido():
    if 'usu' not in session:
        return redirect(url_for('index'))
    return render_template('salida.html', usu=session['usu'])

@app.route('/salir')
def salir():
    session.pop('usu', None)
    flash('Has cerrado sesión.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
