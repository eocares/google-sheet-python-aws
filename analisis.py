from conexion_sheets import obtener_datos


def contar_registros(registros):
    return len(registros)


def agrupar_por_producto(registros):
    resumen = {}
    for registro in registros:
        producto = registro["Producto"]
        cantidad = int(registro["Cantidad"])
        if producto not in resumen:
            resumen[producto] = 0
        resumen[producto] += cantidad
    return resumen


def calcular_ventas(registros):
    total = 0
    for registro in registros:
        cantidad = int(registro["Cantidad"])
        precio = float(registro["Precio"])
        subtotal = cantidad * precio
        total += subtotal
    return total


datos = obtener_datos()
total_registros = contar_registros(datos)
resumen = agrupar_por_producto(datos)
ventas_totales = calcular_ventas(datos)

print("Registros:", total_registros)
print("Unidades:", resumen)
print("Ventas S/:", ventas_totales)