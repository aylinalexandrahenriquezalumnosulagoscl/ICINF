register 
<!DOCTYPE html>
<html>
<head>
    <title>Registro</title>
</head>
<body>
    <h2>Registro</h2>
    {% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
    <form method="POST">
        <input type="text" name="username" placeholder="Correo institucional"><br>
        <input type="password" name="password" placeholder="Contraseña"><br>
        <button type="submit">Registrarse</button>
    </form>
    <p>¿Ya tienes cuenta? <a href="{{ url_for('login') }}">Inicia sesión</a></p>
</body>
</html>

