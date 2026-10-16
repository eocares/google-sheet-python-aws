from analisis import (
    agrupar_por_producto,
    calcular_ventas,
    contar_registros,
)
from conexion_sheets import obtener_datos
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # 1. Obtener datos desde Google Sheets
    datos = obtener_datos()

    # 2. Calcular indicadores
    total_reg = contar_registros(datos)
    total_ven = calcular_ventas(datos)
    resumen_dict = agrupar_por_producto(datos)  # Ej: {'Laptop': 8, 'Mouse': 15}

    # 3. Separar en listas para enviarlas a JavaScript en el HTML
    productos = list(resumen_dict.keys())
    cantidades = list(resumen_dict.values())

    # 4. Enviar variables a dashboard.html
    return render_template(
        "dashboard.html",
        total_registros=total_reg,
        total_ventas=round(total_ven, 2),
        productos=productos,
        cantidades=cantidades,
    )


if __name__ == "__main__":
    app.run(debug=True)