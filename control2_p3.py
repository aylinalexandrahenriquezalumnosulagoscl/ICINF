app
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import re
import json
import os

app = Flask(__name__)
app.secret_key = 'clave-secreta-muy-segura'  # ¡Cambia esto en producción!

# -----------------------------
# Decorador para proteger rutas
# -----------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# -------------------------------------
# Valida que el correo sea institucional
# -------------------------------------
def validar_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@alumnos\.ulagos\.cl$'
    return re.match(pattern, email) is not None

# ------------------------------------
# Cargar y guardar usuarios en JSON
# ------------------------------------
def cargar_usuarios():
    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)

# --------------------------
# Ruta de registro
# --------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        email = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not validar_email(email):
            error = 'El correo debe ser válido y terminar en @alumnos.ulagos.cl'
        elif len(password) < 4:
            error = 'La contraseña debe tener al menos 4 caracteres'
        else:
            usuarios = cargar_usuarios()
            if email in usuarios:
                error = 'El usuario ya existe'
            else:
                usuarios[email] = generate_password_hash(password)
                try:
                    guardar_usuarios(usuarios)
                    return redirect(url_for('login'))
                except Exception:
                    error = 'Error al registrar el usuario'
    return render_template('register.html', error=error)

# --------------------------
# Ruta de login
# --------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        usuarios = cargar_usuarios()

        if email in usuarios and check_password_hash(usuarios[email], password):
            session['usuario'] = email
            return redirect(url_for('dashboard'))
        else:
            error = 'Credenciales incorrectas'
    return render_template('login.html', error=error)

# --------------------------
# Ruta de dashboard protegida
# --------------------------
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', usuario=session['usuario'])

# --------------------------
# Ruta de logout
# --------------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# --------------------------
# Iniciar la app
# --------------------------
if __name__ == '__main__':
    app.run(debug=True)
