# Programa para revisar el inventario y saber que articulos toca pedir
# Problema 3 - Fase 5 - Fundamentos de Programacion

# aqui guardo los articulos: [codigo, nombre, stock actual, stock minimo]
inventario = [
    ["A001", "Teclado inalambrico", 8, 15],
    ["A002", "Mouse optico", 20, 10],
    ["A003", "Monitor 24 pulgadas", 3, 5],
    ["A004", "Diadema con microfono", 12, 12],
    ["A005", "Cable HDMI 2m", 25, 20],
]


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    # si el stock esta bajito respecto al minimo, calculo cuanto falta
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        # si ya hay suficiente, no toca pedir nada
        cantidad = 0
    return cantidad


def generar_lista_de_pedidos(matriz_inventario):
    # con este ciclo reviso articulo por articulo
    print("Lista de pedidos")
    print("-----------------")
    for articulo in matriz_inventario:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        # aqui solo muestro lo que pide el ejercicio: nombre y cantidad
        print(f"{nombre}: pedir {cantidad_pedir} unidades")


def main():
    generar_lista_de_pedidos(inventario)


main()
