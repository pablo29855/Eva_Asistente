from win10toast import ToastNotifier
import speech_recognition as sr
import pyautogui
import time
import random
import threading
import pyttsx3

ruta="\"C:\\Users\\alexa\\Downloads\\SKlauncher 3.1.exe\""
web="https://web.whatsapp.com/"
webYt="www.youtube.com"
name = 'eva'

#FUNCIONES DE LOGICA

def talk(text):
    #CONFIGURACIONES ALEXA
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    #Edita el volumen y voz del asistente
    engine. setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    #Aca se configura el texto para el asistente
    engine.say(text)
    engine.runAndWait()

def conservar_desde_palabra_clave(texto, palabra_clave):
    indice_palabra_clave = texto.find(palabra_clave)

    if indice_palabra_clave != -1:
        texto_conservado = texto[indice_palabra_clave + len(palabra_clave):].strip()
        return texto_conservado.lower()
    else:
        return None

def open_aplication(app):
    pyautogui.hotkey('win', 's')  # Abre la función de búsqueda de Windows
    time.sleep(1)  # Espera un segundo para que se abra la búsqueda
    pyautogui.write(app)  # Escribe "Spotify" en la búsqueda
    time.sleep(1)  # Espera un segundo para que aparezcan los resultados
    pyautogui.press('enter')  # Abre la aplicación de Spotify

def show_notification(text):
    toaster = ToastNotifier()
    toaster.show_toast("Asistente Virtual", ""+text,duration=1,icon_path="img.ico")   

def suspended_assistant():
    nVal = random.randint(0,5)
    if nVal == 1:
        talk("Por supuesto,siempre estoy para ayudarte")
    elif nVal == 2:
        talk("Si, esperando tus ordenes")
    elif nVal == 3:
        talk("Te escucho")
    elif nVal == 4:
        talk("Siempre estoy para ti")
    elif nVal == 5:
        talk("Que deseas que haga")        

def listen():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado. Ningún audio detectado.")
            return None

    try:
        text = r.recognize_google(audio, language='es-CO')
        print("Escuchado:", text)
        result = conservar_desde_palabra_clave(text.lower(),name)
        if 'Eva' in text:
            threading.Thread(target=show_notification(result)).start()
            return result
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz: {0}".format(e))
    
    return None




#DICCIONARIOS O BASE DE DATOS, PALABRAS CONOCIDAS

def google(clave):
    sinonimos1 = {"busque", "buscar", "busca", "búsqueme", "búscame"}
    sinonimos2 = {"qué", "porque"}
    
    claves = clave.split()
    
    for i in range(len(claves) - 1):
        if claves[i] in sinonimos1 or claves[i] in sinonimos2:
            return f"{claves[i]} {claves[i+1]}"
    
    return any(palabra in clave for palabra in sinonimos1 | sinonimos2)

def reproducir(clave):
    sinonimos1 = {"play", "reproduce", "pon", "reproducir", "póngame", "ponme"}
    
    claves = clave.split()
    
    for i in range(len(claves) - 1):
        if claves[i] in sinonimos1:
            return f"{claves[i]} {claves[i+1]}"
    
    return any(palabra in clave for palabra in sinonimos1)

def hora(clave):
    sinonimos1 = {"dime", "dame", "bríndame", "bríndeme", "indíqueme", "muestrame", "muestreme", "regaleme", "regalame", "dígame"}
    sinonimos2 = {"qué hora es", "cual"}
    
    claves = clave.split()
    
    for i in range(len(claves) - 1):
        if claves[i] in sinonimos1:
            return f"{claves[i]} {claves[i+1]}"
    
    return any(palabra in clave for palabra in sinonimos1 | sinonimos2)

def cerrar(clave):
    sinonimos1 = {"cerrar", "closet", "salir", "ciérrate", "finaliza"}
    
    claves = clave.split()
    
    for i in range(len(claves) - 1):
        if claves[i] in sinonimos1:
            return f"{claves[i]} {claves[i+1]}"
    
    return any(palabra in clave for palabra in sinonimos1)

def aplications(clave):
    sinonimos1 = {"valorant", "inicia", "abre", "minecraft"}
    
    claves = clave.split()
    
    for i in range(len(claves) - 1):
        if claves[i] in sinonimos1:
            return f"{claves[i]} {claves[i+1]}"
    
    return any(palabra in clave for palabra in sinonimos1)

def apagar(clave):
    sinonimos1 = {"apagar", "apaga"}
    
    claves = clave.split()
    
    for i in range(len(claves) - 1):
        if claves[i] in sinonimos1:
            return f"{claves[i]} {claves[i+1]}"
    
    return any(palabra in clave for palabra in sinonimos1)

def bloquear(clave):
    sinonimos1 = {"bloquea", "bloquear", "bloqueate"}
    
    claves = clave.split()
    
    for i in range(len(claves) - 1):
        if claves[i] in sinonimos1:
            return f"{claves[i]} {claves[i+1]}"
    
    return any(palabra in clave for palabra in sinonimos1)

def demostracion(clave):
    sinonimos1 = {"demostración", "quien", "sobre", "exhibición", "preséntate", "información"}
    
    claves = clave.split()
    
    for i in range(len(claves) - 1):
        if claves[i] in sinonimos1:
            return f"{claves[i]} {claves[i+1]}"
    
    return any(palabra in clave for palabra in sinonimos1)


def detectar_saludo(clave):
    sinonimos1 = {"buenos", "buen","buenas"}
    sinonimos2 = {"días", "tardes", "noches"}

    claves = clave.split()

    if len(claves) > 1 and claves[0] in sinonimos1 and claves[1] in sinonimos2:
        return f"{claves[0]} {claves[1]}"
