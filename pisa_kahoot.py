# Brenda Elena Saucedo González - A00829855
# 18-13-2020
# Descripción - Reto Versión Completa Pisa Kahoot

# Analisis:
# Datos de entrada: num de opcion del tema y num de respuesta a la pregunta (int)
# Datos de Salida: preguntas y opciones; en caso de necesitar repaso: pregunta, respuesta correcta y frase motivadora (str)
# Proceso Qué?: Preguntar por el numero de tema, y elugo desplegar las preguntas y opciones de ese mismo tema, verificar si es la respuesta correcta,
#               en caso de que no sea asi, desplegar un repaso con la pregunta y su respuesta correcta junto con una frase motivadora.
'''
                                            REFLEXIÓN
En el curso de pensamiento computacional para ingeniería aprendí mucho sobre el lenguaje de programación “Python”,
el cual nunca había oído sobre él. No voy a negar que me enfrente a muchas dificultades al momento de aprender sobre este tipo de lenguaje,
pero me facilito un poco el aprendizaje el que nos pusieran varias entregas para que pudiéramos practicar y aprender más.
En cuanto al reto, me gusto que en el se nos propusiera mejorar el nivel educativo de los jóvenes mexicanos por medio de un programa en Python,
el cual lo hicimos basándonos en el juego de “Kahoot”, para que los jóvenes pudieran estar más preparados para las evaluaciones PISA y al mismo tiempo
más motivados por aprender. También me agrado que el programa fuera un conjunto de temas vistos en clase, para poder practicar y repasarlos.
En general al momento de programar el juego, me tope con varias dificultades para poder desarrollarlo y ejecutarlo correctamente.
Cuando lo checaba, la mayoría de veces me di cuenta que era por error de sintaxis, así que luego de ver los errores en el programa
pude corregirlos. La ventaja de hacer este proyecto con ayuda grupal, es que nos ayudamos para poder encontrar los errores en nuestros programas y
entender que es lo que estaban ejecutando, lo que facilito nuestro aprendizaje y comprensión del programa.
'''
# Importar librerias, para dar color al texto y mezclar las preguntas y sus opciones.
from colorama import init, Fore, Back, Style
import random

# Nota importante - añadí las siguientes funciones para llamarlas desde el programa.
init()
    
def negro():
    return Fore.BLACK

def azul():
    return Fore.BLUE

def celeste():
    return Fore.CYAN

def verde():
    return Fore.GREEN

def rojo():
    return Fore.RED

def magenta():
    return Fore.MAGENTA

def amarillo():
    return Fore.YELLOW


def reset():
    return Fore.RESET


def kahoot(nombre):

    # Inicializar contadores
    preguntas_correctas = 0
    preguntas_repasar = 0

    # Lista de frases motivadoras
    frases = ["No aprendes a caminar siguiendo las reglas. Aprendes haciendo y cayéndote.",
              "El éxito no se da de la noche a la mañana. Es cuando cada día eres mejor que el día anterior.",
              "Aprendiendo demasiado pronto nuestras limitaciones, nunca aprendemos nuestros poderes.",
              "Lo maravilloso de aprender algo, es que nadie puede arrebatárnoslo.",
              "Eso es el aprendizaje. Entender de repente algo que siempre has entendido, pero de una manera nueva.",
              "Los fracasos son una señal de que lo estamos intentando.",
              "Una persona que nunca se ha equivocado es porque nunca a probado nada nuevo.",
              "Todo error deja una enseñanza, toda enseñanza deja una experiencia, y toda experiencia deja una huella.",
              "Levántate, suspira, sonríe, y sigue adelante.",
              "Los retos son lo que hacen la vida interesante, y superarlos es lo que hace que la vida tenga un significado.",
              "La educación es el arma más poderosa que puedes usar para cambiar el mundo.",
              "La mente no es un recipiente para ser llenado, sino un fuego para ser encendido.",
              "La mente una vez iluminada no puede volverse de nuevo oscura.",
              "Cualquiera que deje de aprender es viejo, ya tenga veinte u ochenta años. Cualquier persona que siga aprendiendo permanece joven.",
              "Cuanto más leas, más cosas sabrás. Cuanto más aprendes, a más lugares irás.",
              "La educación es nuestro pasaporte para el futuro, porque el mañana pertenece a la gente que se prepara para él en el día de hoy.",
              "La educación no es para conseguir un trabajo. Se trata de desarrollarte como ser humano.",
              "La sabiduría no es un producto de la escuela, sino del intento de adquirirla para toda la vida.",
              "El gran objetivo de la educación no es el conocimiento sino la acción."]

    # Poner de forma aleatoria las frases
    random.shuffle(frases)
    
    # Lista de colores para que cada opcion se muestre con diferente color
    colores = [celeste(), magenta(), amarillo(), negro()]
    
    # Abrir el archivo de preguntas
    with open (nombre, mode = 'r', encoding = "utf-8") as archivo:
        # Leer todo el archivo y dejarlo en una lista de strings
        lista_preg = archivo.readlines()
        
    # Poner de forma aleatoria las preguntas
    random.shuffle(lista_preg)
    
    # Que voy a almacenar en la lista? - el numero de todas las preguntas erroneas
    lista_preg_repaso = []
    
    # num_preg es el indice, pregunta es el string que esta en ese indice, ciclo para mostrar todas las preguntas de la lista_preg
    # 0, 1, 2, 3, 4
    for num_preg, pregunta in enumerate(lista_preg):

        # Separar todas las partes de la pregunta, usando el separador ≤, split - el split genera una lista de string
        # Enunciado, op1, op2, op3, op4
        lista = pregunta[:-1].split("≤")
        
        # La funcion pop saca el enunciado de la pregunta, borra, elimina el elemento 0 de la lista
        enunciado_preg = lista.pop(0)
        # Salto de linea para que no se junte con el texto anteriormente desplegado
        print()
        # Desplegar la pregunta con su numero
        print(reset(), f'{num_preg + 1}. {enunciado_preg}')
        
        # Crear la lista con las diferentes opciones
        lista_opciones = []
        for opcion in lista:
            # opcion = 'opc1º1'
            # opcion = ['opc1', '1']
            lista_opciones.append(opcion.split('º'))
        
        # Shuffle la lista de opciones
        random.shuffle(lista_opciones)
        
        # Muestra las opciones de respuesta ya desordenadas, en diferentes colores
        for iK, valor in enumerate(lista_opciones):
            print(colores[iK], f'   {iK+1}. {valor[0]}')
        # Quitar el color anterior
        print(reset(), end='')
        
        # Agregar un manejo de excepciones en caso de que el usuario ingrese cualquier otro caracter
        # que no sea un entero y el programa no despliegue un error
        try:
            # Leer la opcion ahora si como entero porque lo usaremos con index de la lista
            respuesta = int(input("Teclea la opcion: "))
        except:
            # En caso de que el usuario ingrese otro caracter, dar como valor a la respuesta 0 para que entre en el ciclo
            respuesta = 0
        
        # Agregar un ciclo por si el usuario tecleo una opcion fuera del rango
        while (respuesta>len(lista_opciones)) or (respuesta<=0):
            # Agregar un manejo de excepciones en caso de que el usuario ingrese cualquier otro caracter
            # que no sea un entero y el programa no despliegue un error
            try:
                # Leer la opcion ahora si como entero porque lo usaremos con index de la lista
                respuesta = int(input("Teclea la opcion: "))
            except:
                # En caso de que el usuario ingrese otro caracter, dar como valor a la respuesta 0 para que vuelva a entrar en el ciclo
                respuesta = 0
        
        # Analizar, revisar y desplegar un mensaje si la opcion ingresada por el usuario es correcta o incorrecta
        if lista_opciones[respuesta-1][1] == '1':
            print("Respuesta correcta")
            preguntas_correctas = preguntas_correctas + 1
        else:
            print("Respuesta incorrecta")
            print("¡Repasar el tema!")
            preguntas_repasar = preguntas_repasar + 1
            # Inserte el num_preg
            lista_preg_repaso.append(num_preg)
    
    # Salto de linea para que no se junte con el texto anteriormente desplegado
    print()

    # Calcular la calificacion total del tematica del cuestionario acorde a las respuestas correctas
    calificacion = int(round((preguntas_correctas/len(lista_preg))*100))

    # Desplegar la calificacion
    print(f'Tu puntuación es: {calificacion} de 100')

    # Esperar a que el usuario ingrese un enter o cualquier otro caracter para continuar con la ejecucion del programa
    pausa = input("< enter >")

    # Salto de linea para que no se junte con el texto anteriormente desplegado
    print()
    
    # Dar un repaso si se tuvo como minimo una respuesta incorrecta
    if preguntas_repasar != 0:

        # Iniciar el repaso
        print("Te vamos a dar un Repaso de las preguntas que tienes que aprender: ")

        # Recorrer la lista de preguntas de repaso
        for iK in lista_preg_repaso:

            # Despues de desplegar la reflexion hacer una pausa para que el alumno reflexione sobre la respuesta
            pausa = input("< enter >")

            # Salto de linea para que no se junte con el texto anteriormente desplegado
            print()
            pregunta = lista_preg[iK]

            # Separar todas las partes de la pregunta, usando el separador ≤, split - el split genera una lista de string
            # Enunciado, op1, op2, op3, op4
            lista = pregunta[:-1].split("≤")

            # La funcion pop saca el enunciado de la pregunta, borra, elimina el elemento 0 de la lista
            enunciado_preg = lista.pop(0)

            # Desplegar la pregunta
            print(rojo(),f'{iK + 1}. {enunciado_preg}')
            
            # Crear la lista con las diferentes opciones
            lista_opciones = []
            for index, opcion in enumerate(lista):
                # opcion = 'opc1º1'
                # opcion = ['opc1', '1']
                lista_opciones.append(opcion.split('º'))
        
            # Muestra solo la respuesta correcta
            for index, valor in enumerate(lista_opciones):
                if valor[1] == '1' :
                    print(negro(), "correcta: ", end="")
                    print(verde(), f'{valor[0]}')
                    
            # Desplegar una frase motivacional
            print(azul(), frases[iK], amarillo())
    
    # En caso contrario, desplegar una felicitacion por responder a todas las preguntas correctamente
    else:
        print('¡Felicitaciones! Respondiste correctamente al cuestionario, sigue así :)')

def menuGrupo838():

    print(reset(),'\nTemas')
    print(rojo(), '1 - Matemáticas')
    print(verde(), '2 - Biología')
    print(negro(), '3 - Inglés')
    print(azul(), '4 - Historia')
    print(rojo(), '5 - Matemáticas')
    print(verde(), '6 - Ciencias')
    print(negro(), '7 - Strings (Programación)')
    print(azul(), '8 - Geografía')
    print(rojo(), '9 - Geografía')
    print(verde(), '10 - Biología')
    print(negro(), '11 - Química')
    print(azul(), '12 - Ciclos (Programación)')
    print(rojo(), '13 - Ciencias')
    print(verde(), '14 - Inglés')
    print(negro(), '15 - Física')
    print(azul(), '16 - Ingresar el nombre del archivo')
    print(verde(), '0 - Salir')

    # Agregar un manejo de excepciones en caso de que el usuario ingrese cualquier otro caracter
    # que no sea un entero y el programa no despliegue un error
    try:
        # Quitar el color anterior
        print(reset(), end='')
        return int(input("Teclea la opcion: "))
    # En caso de que el usuario ingrese otro caracter, dar como valor a la respuesta -1 para que vaya a entrear en el ciclo
    except:
        return -1

def main():

    # Llamar a la funcion menu y desplegar todas las opciones del cuestionario
    opcion = menuGrupo838()
    
    # Ciclo centinela para verificar que el usuario haya ingresado una opcion dentro del rango
    # y diferente de 0 (esta ultima opcion es para salir del programa)
    while opcion != 0:
        # En caso de que la opcion ingresada este dentro del menu, llamar a la funcion kahoot
        if opcion >= 1 and opcion <= 15:
            kahoot("Equipo" + str(opcion) + ".txt")
        # En caso de que la opcion ingresada sea la opcion 16, que el usuario ingrese el nombre del archivo
        elif opcion == 16:
            # Agregar un manejo de excepciones en caso de que el usuario ingrese cualquier otro
            # nombre de archivo que no existe y el programa no despliegue un error
            try:
                kahoot(input("Teclea el nombre del archivo: "))
            # En caso de que el usuario ingrese un el nombre de un archivo que no existe,
            # desplegar un mensaje avisando al usuario de que no se encontro el archivo
            except:
                print("No se encontro el archivo.")
        else:
            print("¡Opción Incorrecta!")
            
        # Esperar a que el usuario ingrese un enter o cualquier otro caracter para continuar con la ejecucion del programa
        pausa = input("< enter >")

        # Salto de linea para que no se junte con el texto anteriormente desplegado
        print()
        
        # Actualizar la vcc
        opcion = menuGrupo838()

# Llamar a la funcion main
main()

'''
                                   Peer Learning 1 (Matemáticas) - Grupo 838
Referencias Bibliografícas:
Anónimo. (2015). Preguntas liberadas de PISA como recursos didácticos de Matemáticas. septiembre 27, 2020, de educaLAB
Sitio web: http://educalab.es/inee/evaluaciones-internacionales/preguntas-liberadas-pisa-piaac/preguntas-pisa-matematicas
'''