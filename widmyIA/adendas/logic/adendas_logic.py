from ..models import Adenda
import string
grafo = {}

def get_todas():
    adendas = Adenda.objects.all()
    return adendas

def procesar_descripcion(descripcion):
    descripcion = descripcion.translate(str.maketrans("", "", string.punctuation))
    palabras = descripcion.split()
    for i in range(len(palabras)-1):
        palabra1 = palabras[i].lower()
        palabra2 = palabras[i+1].lower()
        if palabra1 in grafo:
            if palabra2 in grafo[palabra1]:
                grafo[palabra1][palabra2] += 1
            else:
                grafo[palabra1][palabra2] = 1
        else:
            grafo[palabra1] = {palabra2: 1}

def tres_mas_pesadas(palabra):
    palabra = palabra.translate(str.maketrans("", "", string.punctuation)).lower()
    if palabra not in grafo:
        return None
    
    aristas = grafo[palabra]
    sorted_aristas = sorted(aristas.items(), key=lambda x: x[1], reverse=True)
    palabras_mas_pesadas = [sorted_aristas[i][0] for i in range(min(3, len(sorted_aristas)))]
    print(f"Las palabras más pesadas para {palabra} son: {palabras_mas_pesadas}")
    return palabras_mas_pesadas




def actualizarGrafo():
    adendas = Adenda.objects.all()
    for adenda in adendas:
        descripcion = adenda.descripcion
        procesar_descripcion(descripcion)
    return adendas

def create_adenda(adenda):
    adenda = Adenda(descripcion=adenda["descripcion"])
    adenda.save()
    return adenda

# Ejemplo de uso
procesar_descripcion("Hola tu como estas, espero estes muy bien")
procesar_descripcion("hola, como vas")
procesar_descripcion("hola, como vamos")
print(grafo)
procesar_descripcion("El sol brilla en el cielo.")
procesar_descripcion("La lluvia cae suavemente sobre el tejado.")
procesar_descripcion("Me encanta el olor a café recién hecho.")
procesar_descripcion("La música me hace sentir vivo.")
procesar_descripcion("Me gusta caminar por el parque en otoño.")
procesar_descripcion("Los pájaros cantan en la mañana.")
procesar_descripcion("La naturaleza es impresionante.")
procesar_descripcion("Los colores brillantes me hacen feliz.")
procesar_descripcion("Disfruto leer un buen libro en una tarde tranquila.")
procesar_descripcion("La risa es la mejor medicina.")
procesar_descripcion("El mar es una fuente de tranquilidad para mí.")
procesar_descripcion("Los animales me fascinan.")
procesar_descripcion("La pizza es mi comida favorita.")
procesar_descripcion("El chocolate es la solución a todo.")
procesar_descripcion("Me encanta aprender cosas nuevas.")
procesar_descripcion("La vida es un regalo.")
procesar_descripcion("Los viajes me inspiran.")
procesar_descripcion("Me encanta pasar tiempo con mi familia y amigos.")
procesar_descripcion("El deporte me hace sentir vivo.")
procesar_descripcion("La meditación es una herramienta poderosa para la mente.")
procesar_descripcion("La creatividad es clave en la resolución de problemas.")
procesar_descripcion("El agua es esencial para la vida.")
procesar_descripcion("Me gusta ver el amanecer y el atardecer.")
procesar_descripcion("La fotografía es una forma de capturar recuerdos.")
procesar_descripcion("El baile me hace sentir libre.")
procesar_descripcion("La pintura es una forma de expresión.")
procesar_descripcion("El cine es una forma de escapar de la realidad.")
procesar_descripcion("La tecnología ha revolucionado el mundo.")
procesar_descripcion("La comida picante me hace sentir vivo.")
procesar_descripcion("El vino es una bebida sofisticada.")
procesar_descripcion("La lluvia puede ser muy relajante.")
procesar_descripcion("Me encanta mirar las estrellas en una noche clara.")
procesar_descripcion("El arte es una forma de comunicación universal.")
procesar_descripcion("El respeto es fundamental en cualquier relación.")
procesar_descripcion("La honestidad es la base de cualquier relación.")
procesar_descripcion("El amor es el sentimiento más poderoso.")
procesar_descripcion("La empatía es una habilidad importante para la comprensión de los demás.")
procesar_descripcion("La paciencia es una virtud.")
procesar_descripcion("La música clásica es una forma de arte atemporal.")
procesar_descripcion("El jazz es una forma de expresión única.")
procesar_descripcion("El rock es un género musical que nunca morirá.")
procesar_descripcion("La salsa es un ritmo contagioso.")