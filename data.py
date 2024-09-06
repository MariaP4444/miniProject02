from soundCofiguration import Sound, ListSounds

def get_data():
    story_nodes = {
        "INICIO": {
            "dialog": "Eres Wos, estas trabajando como comerciante del pueblo y es un dia muy ajetreado y extenuante. A las 6 de la tarde cuando el sol se empieza a poner, lo unico que deseas es llegar a casa. Despues de una larga jornada recoges tus cosas y emprendes tu caminata de regreso a casa. Al llegar, te recibe Ness con un abrazo, cenas con tu familia y hablan sobre su dia. Al terminar la cena, quieres ir a dormir pero Ness quiere jugar contigo",
            "sounds": ListSounds([Sound("village.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Jugar con Ness", "siguiente": "JUGAR"},
                2: {"text": "Decirle que pueden jugar otro dia, ahora necesitas descansar", "siguiente": "DESCANSAR"}
            },
            "well_being": 0
        },
        "JUGAR": {
            "dialog": "Ness suelta un chillido de alegria y te toma de la mano",
            "sounds": ListSounds([Sound("childLaugh.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Ir a dormir", "siguiente": "DORMIR"}
            },
            "well_being": 0
        },
        "DESCANSAR": {
            "dialog": "Ness te comprende, pero no oculta su tristeza",
            "sounds": ListSounds([Sound("sigh.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Ir a dormir", "siguiente": "DORMIR"}
            },
            "well_being": 0
        },
        "DORMIR": {
            "dialog": "Hoy es un nuevo dia de trabajo, hay muchas personas en el centro del pueblo. Entre toda la gente llega un sujeto extraño que quiere venderte un mapa de todo el pais, le echas un vistazo, se ve muy antiguo y extraño, las ubicaciones tienen nombres en otro idioma y simbolos extraños. El sujeto dice que es un mapa muy especial, pues indica el camino a la fuente de la vida. Segun la leyenda, de esta fuente brota agua celestial que puede curar cualquier mal.",
            "sounds": ListSounds([Sound("yawn.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Comprar el mapa", "siguiente": "COMPRAR"}
            },
            "well_being": 0
        },
        "COMPRAR": {
            "dialog": "Regresas a casa con el mapa y Davina te dice que Ness no se ha sentido muy bien el día de hoy, entoces deciden llevarla con médico del pueblo. Este la examina detenidamente, finalmente les dice que Ness tiene una enfermedad muy grave que apenas se está desarrollando rapidamente y le da unos dias de vida. En ese momento, recuerdas el mapa misterioso y decides tomar una desicion arriesgada.",
            "sounds": ListSounds([Sound("coins.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Decides emprender un viaje en busca de la fuente de la vida", "siguiente": "AVENTURA"},
                2: {"text": "Decides aceptar el diagnostico", "siguiente": "RESIGNARSE"}
            },
            "well_being": 0
        },
        "RESIGNARSE": {
            "dialog": "Decides pasar con tu hija sus ultimos momentos",
            "sounds": ListSounds([Sound("sad.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {},
            "well_being": 0
        },
        "AVENTURA": {
            "dialog": "Al emprender este viaje debes llevar recursos que te ayuden a sobrevivir, pero no puedes llevar tu maleta muy cargada por lo que solo tienes la posibilidad de llevar comida:",
            "sounds": ListSounds([Sound("food.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Empacar comida y salir", "siguiente": "OPCION1"}
            },
            "well_being": 0
        },
        "OPCION1": {
            "dialog": "Te despides de Ness y Davina. Segun el mapa, puedes ir por dos caminos hacia tu destino: En el primero tienes que pasar por IceWind, un area sometida en un eterno invierno y desolada. Por otra parte, tienes que atravesar las montañas de Wolls, estas son conocidas por albergar una gran cantidad de criaturas desconocidas y peligrosas. Haz tu desicion",
            "sounds": ListSounds([Sound("adventure.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Tomar el camino de IceWind", "siguiente": "ICEWIND1"},
                2: {"text": "Tomar el camino de Wolls", "siguiente": "WOLLS1"}
            },
            "well_being": 0
        },
        "WOLLS1": {
            "dialog": "Despues de unas horas de caminata se va haciendo de noche y decides que es hora de una parada, encuentras una pequenia casa en la que vive una mujer con sus hijos y le pides que te de posada, ella lo hace con la condicion de que le des la mitad de tu comida.",
            "sounds": ListSounds([Sound("stepsDirt.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Darle la mitad de la comida y dormir en su casa.", "siguiente": "ACEPTAR1"},
                2: {"text": "Seguir el camino hasta el amanecer.", "siguiente": "RECHAZAR1"}
            },
            "well_being": 0
        },

        "ACEPTAR1": {
            "dialog": "Duermes en el suelo, cerca de la chimenea y logras descansar lo suficiente para seguir tu camino. Al siguiente dia comes un tercio de la comida que te queda",
            "sounds": ListSounds([Sound("fire.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {},
            "well_being": 0
        },
        "RECHAZAR1": {
            "dialog": "Sigues caminando toda la noche. Al amanecer tienes mucho cansancio y hambre.",
            "sounds": ListSounds([Sound("night.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Comer la mitad de la comida para tener suficiente energia", "siguiente": "COMER1"},
                2: {"text": "Ignorar el hambre", "siguiente": "SEGUIR1"}
            },
            "well_being": 0
        },
        "COMER1": {
            "dialog": "Mientras atraviesas los arboles con el rio a tu derecha, escuchas un grunido tenebroso a tu izquierda, es un monstruo que se acerca",
            "sounds": ListSounds([Sound("BeastGrowl.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Correr todo lo que pueda", "siguiente": "CORRERW1"},
                2: {"text": "Coger piedras y lanzarselas", "siguiente": "ATACARW1"}
            },
            "well_being": 0
        },
        "SEGUIR1": {
            "dialog": "Mientras atraviesas los arboles con el rio a tu derecha, escuchas un grunido tenebroso a tu izquierda, es un monstruo que se acerca",
            "sounds": ListSounds([Sound("BeastGrowl.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Correr todo lo que pueda", "siguiente": "CORRERW1"},
                2: {"text": "Coger piedras y lanzarselas", "siguiente": "ATACARW1"}
            },
            "well_being": -20
        },
        "CORRERW1": {
            "dialog": "El monstruo te lanza una baba que te quema la piel de toda la espalda.",
            "sounds": ListSounds([Sound("runningDirt.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Correr hacia el rio", "siguiente": "RIOW1"}
            },
            "well_being": -30
        },
        "ATACARW1": {
            "dialog": "El monstruo se lanza sobre ti, quemandote gran parte de la piel",
            "sounds": ListSounds([Sound("RockImpacts.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Correr hacia el rio", "siguiente": "RIOW1"}
            },
            "well_being": -60
        },
        "RIOW1": {
            "dialog": "Finalmente, logras meterte en el rio y el monstruo ya no puede perseguirte. Ahora tienes que luchar contra la corriente y las rocas",
            "sounds": ListSounds([Sound("splash.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Nadar con todas tus fuerzas", "siguiente": "NADARW1"}
            },
            "well_being": -20
        },
        "NADARW1": {
            "dialog": "Al salir del rio tienes tu camino, miras el mapa, el cual milagrosamente sigue intacto y ves que estas muy cerca de tu destino.",
            "sounds": ListSounds([Sound("river.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Mirar mapa", "siguiente": "MAPA"}
            },
            "well_being": 0
        },
        "ICEWIND1": {
            "dialog": "Despues de unas horas de caminata se va haciendo de noche y decides que es hora de una parada, puedes entrar en una cueva o en una choza aparentemente abandonada.",
            "sounds": ListSounds([Sound("night.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Entrar en la choza", "siguiente": "CHOZA1"},
                2: {"text": "Entrar en la cueva", "siguiente": "CUEVA1"}
            },
            "well_being": 0
        },
        "CHOZA1": {
            "dialog": "Al entrar encuentras un lugar comodo para dormir, pero tal vez no sea muy seguro.",
            "sounds": ListSounds([Sound("night.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Dormir", "siguiente": "DORMIRCH1"},
                2: {"text": "Quedarse despierto", "siguiente": "VIGILIACH1"}
            },
            "well_being": 0
        },
        "DORMIRCH1": {
            "dialog": "Ha empezado un incendio en la choza mientras estabas dormido, cuando te despiertas todo tu alrededor esta en llamas y al tratar de huir quedas malherido.",
            "sounds": ListSounds([Sound("fire.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Salir de la choza", "siguiente": "SALIR"}
            },
            "well_being": -55
        },
        "VIGILIACH1": {
            "dialog": "En mitad de la noche escuchas pisadas muy suaves en la choza y decides investigar, un duende esta intentando prender fuego a la choza pero logras detenerlo. La vigilia te ha quitado energias.",
            "sounds": ListSounds([Sound("night.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Salir de la choza", "siguiente": "SALIR"}
            },
            "well_being": -15
        },
        "SALIR": {
            "dialog": "Sigues tu camino durante largas horas tranquilamente, parece que estas cerca.",
            "sounds": ListSounds([Sound("runningDirt.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Seguir el camino", "siguiente": "CAMINO"}
            },
            "well_being": 0
        },

        "CUEVA1": {
            "dialog": "Te sientas en la cueva y encuentras un lugar lo suficientemente calido para descansar. Debates entre dormir o estar despierto toda la noche.",
            "sounds": ListSounds([Sound("stepsDirt.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Dormir", "siguiente": "DORMIRC1"},
                2: {"text": "Quedarse despierto", "siguiente": "VIGILIAC1"}
            },
            "well_being": 0
        },
        "VIGILIAC1": {
            "dialog": "Empiezas a escuchar lobos detras de ti, no tienes nada con que defenderte.",
            "sounds": ListSounds([Sound("night.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Coger tu maleta y huir lo mas lejos que puedas", "siguiente": "CORRER1"},
                2: {"text": "Quedarte quieto", "siguiente": "QUIETO1"},
                3: {"text": "Atacar a los lobos", "siguiente": "ATACAR1"}
            },
            "well_being": 0
        },
        "CORRER1": {
            "dialog": "Corres lo mas rapido que puedes y logras huir de los lobos.",
            "sounds": ListSounds([Sound("runningDirt2.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Mirar mapa", "siguiente": "MAPA"}
            },
            "well_being": 0
        },
        "QUIETO1": {
            "dialog": "Los lobos te rodean, pero finalmente te dejan en paz. Te quedas la noche en vela.",
            "sounds": ListSounds([Sound("Wolfgrowling.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Mirar mapa", "siguiente": "MAPA"}
            },
            "well_being": -10
        },
        "ATACAR1": {
            "dialog": "Los lobos te agarran los brazos y te atacan sin piedad.",
            "sounds": ListSounds([Sound("Wolfgrowling.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Mirar mapa", "siguiente": "MAPA"}
            },
            "well_being": -50
        },
        "DORMIRC1": {
            "dialog": "Recargas energias toda la noche, pero al despertar te das cuenta que tu comida no esta, parece que un animal se la ha devorado... Sigues tu camino, pero no mucho despues te ataca el hambre. Ves un arbol del que cuelga una fruta extraña que nunca habías visto.",
            "sounds": ListSounds([Sound("sunrise.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Coger una piedra y lanzarla al arbol para comer la fruta", "siguiente": "LANZARF1"},
                2: {"text": "Desconfiar de la fruta y seguir el camino", "siguiente": "IGNORARF1"}
            },
            "well_being": 0
        },
        "LANZARF1": {
            "dialog": "La fruta desconocida te ha hecho mal. Te duele el estomago y quieres vomitar.",
            "sounds": ListSounds([Sound("throw.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Mirar mapa", "siguiente": "MAPA"}
            },
            "well_being": -40
        },
        "MAPA": {
            "dialog": "Al abrir el mapa te das cuenta que estas muy cerca de tu destino. Pero te encuentras con un Goblin que cuida la fuente de la vida.",
            "sounds": ListSounds([Sound("mapa.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Atacar al Goblin", "siguiente": "PELEA"},
                2: {"text": "Intentar hablar con el", "siguiente": "HABLAR"}
            },
            "well_being": 0
        },
        "PELEA": {
            "dialog": "Luchas con el Goblin a muerte.",
            "sounds": ListSounds([Sound("pelea.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Matar al Goblin", "siguiente": "MATAR"}
            },
            "well_being": -70
        },
        "MATAR": {
            "dialog": "Logras conseguir el agua de la vida, pero estas demasiado debil para regresar a casa. Mueres a mitad de camino.",
            "sounds": ListSounds([Sound("dolor.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {},
            "well_being": 0
        },
        "HABLAR": {
            "dialog": "El Goblin solo te dejara tomar de la fuente de la vida si respondes una pregunta correctamente, de lo contrario, te matara. La pregunta es: ¿Porque decidiste estudiar sistemas?",
            "sounds": ListSounds([Sound("Gruñidos.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {
                1: {"text": "Por plata obvi", "siguiente": "R1"},
                2: {"text": "Por pasion", "siguiente": "R2"}
            },
            "well_being": 0
        },
        "R1": {
            "dialog": "El Goblin esta decepcionado de tu respuesta, has muerto.",
            "sounds": ListSounds([Sound("death.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {},
            "well_being": -100
        },
        "R2": {
            "dialog": "El Goblin te deja sacar de la fuente de la vida y te lleva de regreso a casa sano y a salvo. Logras salvar a tu hija de su fatal destino y viven felices para siempre.",
            "sounds": ListSounds([Sound("sunrise.wav", (-3, 0, 0), 0.5, (0, 0, 0))]),
            "options": {},
            "well_being": 0
        }


    }
    return story_nodes