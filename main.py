from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Simulamos una base de datos con usuarios
USUARIOS = {
    "admin": "12345",
    "logistica1": "transporte2025",
    "supervisor": "almacen123"
}

# Página principal (login)
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        clave = request.form["clave"]

        if usuario in USUARIOS and USUARIOS[usuario] == clave:
            return redirect(url_for("dashboard", usuario=usuario))
        else:
            return "<h3>❌ Usuario o contraseña incorrectos</h3>"
    
    # HTML simple del formulario
    return render_template_string("""
    <h2>🚚 Login - Empresa de Logística</h2>
    <form method="post">
        Usuario: <input type="text" name="usuario"><br><br>
        Contraseña: <input type="password" name="clave"><br><br>
        <button type="submit">Ingresar</button>
    </form>
    """)

# Página del dashboard
@app.route("/dashboard/<usuario>")
def dashboard(usuario):
    return f"<h2>Bienvenido {usuario} 👋</h2><p>Panel de control de la empresa de logística.</p>"

if __name__ == "__main__":
    app.run(debug=True)
