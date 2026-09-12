# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Pokedex
- Por qué lo eligieron (5–8 líneas): 
> Porque nos pareció interesate el tema. Ambos integrantes del grupo lo conocemos por el anime y/o juegos que consumiamos en nuestra infancia. Así que nos pareció buena idea elegirlo como nuestra tema a trabajar. Ademas notamos que tiene bastantes datos interesantes que, a diferencia de las canciones o las recetas, nos resultó mas adecuado a nuestra visión de trabajo. En fin, nos gustan los juegos a los 2.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

> Un item de catalogo es un objeto con 'identidad propia' creado a partir de una clase, como lo es en nuestro caso, y que dicho objeto tiene sus atributos definidos. Nosotros usamos los atributos de la pestaña CSV para hacer la lista (catalogo) en donde se encuentran todos los pokemones. Los atributos son: id (le pusimos 'iden' por una cuestion de sintaxis), nombre, tipo 1, tipo 2, puntos de vida, ataque, defenza, velocidad, generación.
> Mutable podemos definir aquellos datos que pueden ser modificados, por ejemplo las listas, los diccionarios, los conjuntos, podemos añadir mas datos, quitarlos, cambiarlos... En cambio los inmutables son aquellos a los que no podemos modificar, por ejemplo una string, donde cada caracter es un elemento con un valor definido. Por ejemplo, al indexar una str no podemos cambiar el valor de la letra a la que llamamos con el indice. Lo mismo sucede con los numeros (int, float), con las tuplas... Nosotros elegimos una lista para hacer nuestro catalogo porque la idea es poder modificar ducha lista agregando mas pokemones o en otros casos, sacarlos de la lista mediante la consola.
>El catalogo son los items que tenemos agregados a nuestra colección principal, que es la lista, valga la redundancia, llamada 'catalogo'. Si yo quiero deshacer o eliminar el ultimo elemento agregado a la lista puedo usar el metodo .pop(), eso seria la PILA, como si la lista guardara un historial de lo ultimo en entrar. Si quiero procesar o sacar el primero de la lista, usaria el metodo .popleft(), eso seria COLA, seria 'atender' los items por 'orden de llegada'.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
