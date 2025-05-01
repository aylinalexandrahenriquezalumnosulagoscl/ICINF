login
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Iniciar Sesión</h2>
    {% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
    <form method="POST">
        <input type="text" name="username" placeholder="Correo institucional"><br>
        <input type="password" name="password" placeholder="Contraseña"><br>
        <button type="submit">Entrar</button>
    </form>
    <p>¿No tienes cuenta? <a href="{{ url_for('register') }}">Regístrate</a></p>
</body>
</html>

