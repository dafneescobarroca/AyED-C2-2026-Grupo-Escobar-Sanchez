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
    7:[8],8:[9],
    10:[11],11:[12],
    16:[17],17:[18],
    19:[20],
    35:[36],
    37:[38],
    43:[44],44:[45],
    58:[59],
    63:[64],64:[65],
    66:[67],67:[68],
    74:[75],75:[76],
    81:[82],
    92:[93],93:[94],
    129:[130],
    147:[148],148:[149],
    152:[153],153:[154],
    155:[156],156:[157],
    175:[176],
    179:[180],180:[181],
    246:[247],247:[248],
    
}
def mostrar_evoluciones(pokemon_id):
    print(buscar_nombre(pokemon_id), end="")
    if pokemon_id not in evoluciones:
        return
    for siguiente_id in evoluciones[pokemon_id]:
        print("→",end="")
        mostrar_evoluciones(siguiente_id)

pokemones_base= [172,1,4,133,7,10,16,19,35,37,43,58,63,66,74,81,92,95,129,137,147,150,151,152,155,175,179,246]

def mostrar_todas_las_evoluciones():
    for base in pokemones_base:
        mostrar_evoluciones(base)
        print()