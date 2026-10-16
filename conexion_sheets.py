# conexion_sheets.py
import gspread


def obtener_datos():
    # Autenticación mediante credenciales de Google Cloud
    cliente = gspread.service_account(filename="credenciales.json")

    # Abrir la hoja de cálculo por su ID
    archivo = cliente.open_by_key("1rnRaD7koIQbQ1Ncu2RKpur6Qgy5jCuJmLz2ms8lgZkw")

    # Seleccionar la primera hoja
    hoja = archivo.sheet1

    # Leer todos los registros
    datos = hoja.get_all_records()

    return datos


# Este bloque SOLO se ejecuta si corres 'python conexion_sheets.py' directamente
if __name__ == "__main__":
    # Autenticamos para obtener el título en la prueba individual
    cliente_prueba = gspread.service_account(filename="credenciales.json")
    archivo_prueba = cliente_prueba.open_by_key(
        "1rnRaD7koIQbQ1Ncu2RKpur6Qgy5jCuJmLz2ms8lgZkw"
    )

    print("¡Conexión exitosa!")
    print(f"Título de la hoja: {archivo_prueba.title}")

    datos = obtener_datos()
    print(f"Datos recuperados correctamente. Total de filas: {len(datos)}")
