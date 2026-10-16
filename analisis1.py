from conexion_sheets import obtener_datos


def contar_registros(registros):
    """Cuenta la cantidad total de transacciones/registros."""
    return len(registros)


def agrupar_por_producto(registros):
    """Calcula la cantidad total de unidades vendidas por producto."""
    resumen = {}
    for registro in registros:
        producto = registro["Producto"]
        cantidad = int(registro["Cantidad"])
        resumen[producto] = resumen.get(producto, 0) + cantidad
    return resumen


def calcular_ventas(registros):
    """Calcula el monto total de ventas en dinero."""
    total = 0.0
    for registro in registros:
        cantidad = int(registro["Cantidad"])
        precio = float(registro["Precio"])
        total += cantidad * precio
    return total


def calcular_ingresos_por_producto(registros):
    """Calcula la recaudación en dinero generada por cada producto."""
    ingresos = {}
    for registro in registros:
        producto = registro["Producto"]
        subtotal = int(registro["Cantidad"]) * float(registro["Precio"])
        ingresos[producto] = ingresos.get(producto, 0.0) + subtotal
    return ingresos


def obtener_producto_top(ingresos):
    """Encuentra el producto que generó mayores ingresos."""
    if not ingresos:
        return None, 0.0
    prod_top = max(ingresos, key=ingresos.get)
    return prod_top, ingresos[prod_top]


def main():
    # Obtener los datos desde Google Sheets
    datos = obtener_datos()

    if not datos:
        print("No se encontraron registros para analizar.")
        return

    # Cálculos principales
    total_registros = contar_registros(datos)
    unidades_por_producto = agrupar_por_producto(datos)
    ventas_totales = calcular_ventas(datos)
    ingresos_por_producto = calcular_ingresos_por_producto(datos)
    prod_top, ingreso_top = obtener_producto_top(ingresos_por_producto)
    ticket_promedio = ventas_totales / total_registros if total_registros > 0 else 0

    # Presentación de resultados en terminal
    print("\n==================================================")
    print("           REPORTE AVANZADO DE VENTAS             ")
    print("==================================================")
    print(f"📊 Total de transacciones: {total_registros}")
    print(f"💰 Ventas Totales: S/ {ventas_totales:,.2f}")
    print(f"🎟️ Ticket Promedio por venta: S/ {ticket_promedio:,.2f}")
    print("--------------------------------------------------")
    print("📦 Unidades vendidas por producto:")
    for prod, cant in unidades_por_producto.items():
        print(f"   • {prod}: {cant} unidades")
    print("--------------------------------------------------")
    print("💵 Ingresos por producto:")
    for prod, monto in ingresos_por_producto.items():
        print(f"   • {prod}: S/ {monto:,.2f}")
    print("--------------------------------------------------")
    print(f"🏆 Producto más rentable: {prod_top} (S/ {ingreso_top:,.2f})")
    print("==================================================\n")


if __name__ == "__main__":
    main()
