tem code
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Ruta del archivo JSON
USUARIOS_JSON = os.path.join(os.path.dirname(__file__), 'data', 'usuarios.json')

# Cargar usuarios desde JSON o crear archivo si no existe
def cargar_usuarios():
    if not os.path.exists(USUARIOS_JSON):
        with open(USUARIOS_JSON, 'w') as f:
            json.dump({"admin@alumnos.ulagos.cl": generate_password_hash('1234')}, f)
    
    with open(USUARIOS_JSON, 'r') as f:
        return json.load(f)

# Guardar usuarios en JSON
def guardar_usuarios(usuarios):
    with open(USUARIOS_JSON, 'w') as f:
        json.dump(usuarios, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        usuarios = cargar_usuarios()
        
        if email in usuarios and check_password_hash(usuarios[email], password):
            session['usuario'] = email
            return redirect(url_for('dashboard'))
        else:
            error = 'Usuario o contraseña incorrectos'
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        usuarios = cargar_usuarios()
        
        if '@alumnos.ulagos.cl' not in email:
            error = 'El correo debe ser @alumnos.ulagos.cl'
        elif email in usuarios:
            error = 'El usuario ya existe'
        else:
            usuarios[email] = generate_password_hash(password)
            guardar_usuarios(usuarios)
            return redirect(url_for('login'))
    return render_template('register.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return f"Bienvenido {session['usuario']} a tu panel de control. <a href='/logout'>Cerrar sesión</a>"
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Crear carpeta 'data' si no existe
    os.makedirs(os.path.dirname(USUARIOS_JSON), exist_ok=True)
    app.run(debug=True)

