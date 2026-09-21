from src.dominio.pokemones import catalogo
def buscar_nombre(pokemon_id):
    for pokemon in catalogo:
        if pokemon.iden == pokemon_id:
            return pokemon.nombre
    return "Pokemon no encontrado"
evoluciones= {
    172:[25],
    25:[26]
}
def mostrar_evoluciones(pokemon_id):
    print(buscar_nombre(pokemon_id))
    if pokemon_id not in evoluciones:
        return
    for siguiente_id in evoluciones[pokemon_id]:
        mostrar_evoluciones(siguiente_id)
