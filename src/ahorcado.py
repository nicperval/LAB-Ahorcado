import random
def cargar_palabras(ruta):
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip())
        return res
    
def elegir_palabra(PALABRAS):
    return random.choice(PALABRAS)
    
def enmascarar_palabra(palabra, letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la lista 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena concatenando los elementos de la lista (ver 'Ayuda')
    Ayuda: 
    - Utilice el método join de las cadenas. Observe el siguiente ejemplo:
        ' '.join(['a','b','c']) # Devuelve "a b c"
    '''
    lista = []
    for i in palabra:
            if i in letras_probadas:
                lista.append(i)
            else:
                lista.append('_')
         
    return ' '.join(lista)

def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    '''
    nueva_letra_normal = input(f"Introduzca una letra a probar, (si introduce mas de un valor, se utilizara el ultimo): ")
    while nueva_letra_normal[-1].isalpha() == False:
        nueva_letra_normal = input("Por favor, introduzca una letra: ")
    nueva_letra = nueva_letra_normal[-1].lower()
    while nueva_letra in letras_probadas:
        nueva_letra_normal = input(f"Ya has probado con esta letra, introduce una nueva: ")
        while nueva_letra_normal[-1].isalpha() == False:
            nueva_letra_normal = input("Por favor, introduzca una letra: ")
    nueva_letra = nueva_letra_normal.lower()
    return nueva_letra

def comprobar_letra(palabra_secreta, letra):
    '''
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Mostrar el mensaje correspondiente informando al usuario
    - Devolver True si estaba y False si no
    '''
    if letra in palabra_secreta:
        return True
    else:
        return False
    
def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    '''
    lista = []
    if len(letras_probadas) == 0:
        return False
    else:
        for i in letras_probadas:
            if i in palabra_secreta:
                lista.append(1)
            else:
                lista.append(0)
        if sum(lista) == len(palabra_secreta):
            return True
        else:
            return False
        
def ejecutar_turno(palabra_secreta, letras_probadas):
    '''
    Ejecutar un turno de juego:
    - Mostrar la palabra enmascarada
    - Pedir la nueva letra
    - Comprobar si la letra está en la palabra (acierto) o no (fallo)
    - Añadir la letra al conjunto de letras probadas
    - Devolver True si la letra fue un acierto, False si fue un fallo
    Ayuda:
    - Recuerda las funciones que ya has implementado para mostrar la palabra, pedir la letra y comprobarla
    '''
    print(enmascarar_palabra(palabra_secreta,letras_probadas))
    letra = pedir_letra(letras_probadas)
    letras_probadas.append(letra)
    intento = comprobar_letra(palabra_secreta,letra)
    return intento
    print(letras_probadas)

def jugar(max_intentos, palabras):
    '''
    Completar una partida hasta que el jugador gane o pierda:
    - Mostrar mensaje de bienvenida
    - Elegir la palabra secreta a adivinar
    - Inicializar las variables del juego (letras probadas e intentos fallidos)
    - Ejecutar los turnos de juego necesarios hasta finalizar la partida, y en cada turno:
      > Averiguar si ha habido acierto o fallo
      > Actualizar el contador de fallos si es necesario
      > Comprobar si se ha superado el número de fallos máximo
      > Comprobar si se ha completado la palabra
      > Mostrar el mensaje de fin adecuado si procede o el número de intentos restantes
    '''
    print("¡Bienvenido al ahorcado!")
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    palabra_secreta = elegir_palabra(palabras)
    letras_probadas = []
    
    while max_intentos != 0:
        x = ejecutar_turno(palabra_secreta,letras_probadas)
        if x == False:
            max_intentos -= 1
        y = comprobar_palabra_completa(palabra_secreta,letras_probadas)
        if y == True:
            print(f'Felicidades, acertaste la palabra "{palabra_secreta}"')
    print("Esperamos verte pronto otra vez")

if __name__ == "__main__":
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    jugar(30, palabras)