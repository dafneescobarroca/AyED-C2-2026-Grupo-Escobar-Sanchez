class pokemon:
    def __init__(self,iden,nombre,tipo1,tipo2,hp,ataque,defensa,velocidad,generacion):
        self.iden = iden
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion 

catalogo= [
    pokemon(1,"Bulbasaur","Planta","Veneno",45,49,49,45,1) ,
    pokemon(2,"Ivysaur","Planta","Veneno",60,62,63,60,1) ,
    pokemon(3,"Venusaur","Planta","Veneno",80,82,83,80,1),
    pokemon(4,"Charmander","Fuego","-",39,52,43,65,1),
    pokemon(5,"Charmeleon","Fuego","-",58,64,58,80,1),
    pokemon(6,"Charizard","Fuego","Volador",78,84,78,100,1),
    pokemon(7,"Squirtle","Agua","-",44,48,65,43,1),
    pokemon(8,"Wartortle","Agua","-",59,63,80,58,1),
    pokemon(9,"Blastoise","Agua","-",79,83,100,78,1),
    pokemon(10,"Caterpie","Bicho","-",45,30,35,45,1),
    pokemon(11,"Metapod","Bicho","-",50,20,55,30,1) ,
    pokemon(12,"Butterfree","Bicho","Volador",60,45,50,70,1),
    pokemon(16,"Pidgey","Normal","Volador",40,45,40,56,1),
    pokemon(17,"Pidgeotto","Normal","Volador",63,60,55,71,1),
    pokemon(18,"Pidgeot","Normal","Volador",83,80,75,101,1),
    pokemon(19,"Rattata","Normal","-",30,56,35,72,1),
    pokemon(20,"Raticate","Normal","-",55,81,60,97,1),
    pokemon(25,"Pikachu","Electrico","-",35,55,40,90,1),
    pokemon(26,"Raichu","Electrico","-",60,90,55,110,1),
    pokemon(35,"Clefairy","Hada","-",70,45,48,35,1),
    pokemon(35,"Clefairy","Hada","-",70,45,48,35,1),
    pokemon(37,"Vulpix","Fuego","-",38,41,40,65,1),
    pokemon(38,"Ninetales","Fuego","-",73,76,75,100,1),
    pokemon(43,"Oddish","Planta","Veneno",45,50,55,30,1),
    pokemon(44,"Gloom","Planta","Veneno",60,65,70,40,1),
    pokemon(45,"Vileplume","Planta","Veneno",75,80,85,50,1),
    pokemon(58,"Growlithe","Fuego","-",55,70,45,60,1),
    pokemon(59,"Arcanine","Fuego","-",90,110,80,95,1),
    pokemon(63,"Abra","Psiquico","-",25,20,15,90,1),
    pokemon(64,"Kadabra","Psiquico","-",40,35,30,105,1),
    pokemon(65,"Alakazam","Psiquico","-",55,50,45,120,1),
    pokemon(66,"Machop","Lucha","-",70,80,50,35,1),
    pokemon(67,"Machoke","Lucha","-",80,100,70,45,1),
    pokemon(68,"Machamp","Lucha","-",90,130,80,55,1),
    ]
   