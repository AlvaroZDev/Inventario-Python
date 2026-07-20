# Inventario

## Explicación del Funcionamiento del Programa

El programa parte de una matriz llamada `inventario`, donde cada fila guarda el código, el nombre, el stock actual y el stock mínimo requerido de un artículo.

La función `calcular_cantidad_a_pedir` recibe el stock actual y el stock mínimo de un artículo y los compara:
- si el stock actual es menor que el mínimo, calcula la diferencia entre ambos y esa es la cantidad que hay que pedir;
- si el stock actual ya es igual o mayor al mínimo, la función devuelve cero porque no hace falta pedir nada.

La función `generar_lista_de_pedidos` recorre la matriz completa con un ciclo `for`. Para cada artículo, toma el nombre, el stock actual y el stock mínimo, llama a la función anterior para saber cuánto pedir y muestra en pantalla el nombre del artículo junto con esa cantidad.

La función `main()` es la que se encarga de iniciar todo el proceso cuando se ejecuta el archivo desde la consola.
