index 
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Inicio</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="heart">
        <p>Bienvenido ❤️<br>
        <a href="/login" style="color: white;">Iniciar sesión</a> |
        <a href="/register" style="color: white;">Registrarse</a>
        </p>
    </div>
</body>
</html>

