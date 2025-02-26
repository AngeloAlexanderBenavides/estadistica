from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

# Ruta para la página principal (index.html)
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para la página secundaria (grafica.html)
@app.route("/grafica")
def grafica():
    return render_template("grafica.html")

# Ruta para la página de entrada de datos (paginas.html)
@app.route("/paginas_html")
def paginas_html():
    return render_template("paginas.html")

# Ruta para manejar la solicitud POST y calcular el factor Z
@app.route("/paginas", methods=["POST"])  
def paginas():
    # Obtener los datos del cuerpo de la solicitud
    data = request.get_json()

    # Extraer los valores
    media = float(data.get("media"))
    limite_superior = float(data.get("limiteSuperior"))
    limite_inferior = float(data.get("limiteInferior"))

    # Validar que los datos estén presentes
    if not all([media, limite_superior, limite_inferior]):
        return jsonify({"error": "Faltan datos"}), 400

    # Calcular la media poblacional (μ) y la desviación estándar (σ)
    mu = (limite_superior + limite_inferior) / 2  # Media poblacional
    sigma = (limite_superior - limite_inferior) / 6  # Desviación estándar (asumiendo 6σ)

    # Calcular el factor Z
    z = (media - mu) / sigma

    # Devolver los resultados en formato JSON
    return jsonify({
        "media": media,
        "mu": mu,
        "sigma": sigma,
        "z": z,
    })

# Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)