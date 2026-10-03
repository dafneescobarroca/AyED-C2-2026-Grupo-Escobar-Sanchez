from src.dominio.pokemones import catalogo
def buscar_nombre(pokemon_id):
    for pokemon in catalogo:
        if pokemon.iden == pokemon_id:
            return pokemon.nombre
    return "Pokemon no encontrado"
evoluciones= {
    172:[25],25:[26],
    1:[2],2:[3],
    4:[5],5:[6],
    133:[134,135,136],

}
def mostrar_evoluciones(pokemon_id):
    print(buscar_nombre(pokemon_id), end="")
    if pokemon_id not in evoluciones:
        return
    for siguiente_id in evoluciones[pokemon_id]:
        print("→",end="")
        mostrar_evoluciones(siguiente_id)
pokemones_base= [172,1,4,133]
def mostrar_todas_las_evoluciones():
    for base in pokemones_base:
        mostrar_evoluciones(base)
        print()