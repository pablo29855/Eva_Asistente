from unidecode import unidecode
import pywhatkit
import pyautogui
import webbrowser as web
import datetime
import datetime
import os
import datos
import time


def run():
    while True:
        rec=datos.listen()
        if(rec==None):
            return 0
        
        clave = rec.split()[0]
        
        if 'estás ahí' in rec:
            datos.suspended_assistant()

        #REPRODUCIR EN YOUTUBE
        elif datos.reproducir(rec):  
            val = rec.replace(clave, '')
            print("=======Reproduciendo========")
            datos.talk('Reproduciendo ' + val)
            pywhatkit.playonyt(val)    
            break 
        #BUSQUEDA EN GOOGLE    
        elif datos.google(rec):
            val=rec.replace(clave,'')
            print("========Buscando==========")
            datos.talk('Realizando busqueda'+val)
            url="https://www.google.com/search?q="
            search_url  = url+val
            web.open(search_url)
            break
        #HORA 
        elif datos.hora(rec):      
            val = datetime.datetime.now().strftime('%I:%M %p')
            datos.talk("Son las "+val)
            print("=========Hora===========")
            print("======="+val+"==========")
            print("\t\t\t\t\t\t\t\t\t")
            break
        #CERRAR ASISTENTE    
        elif datos.cerrar(rec):
            datos.talk("Cerrando asistente")
            return 1      

        elif datos.aplications(rec):
            val=rec.replace(clave,'')
            if(val.split()[0]=="minecraft"):
                datos.talk("iniciando "+val)
                os.system(datos.ruta)
            elif(val.split()[0]=="whatsapp" and val.split()[1]=="web"):
                datos.talk("abriendo whatsapp web")   
                web.open(datos.web)
            elif(val.split()[0]=="youtube"):
                datos.talk("abriendo youtube")
                web.open(datos.webYt)
            else:
                datos.talk("abriendo "+val)
                datos.open_aplication(unidecode(val))
            break        

        if datos.apagar(rec):
            val=rec.replace(clave,'')
            datos.talk("Apagando equipo. Descansa")
            os.system("shutdown /s /t 1")
            break

        if datos.bloquear(rec):
            al=rec.replace(clave,'')
            datos.talk("Bloqueando equipo.")
            os.system("rundll32.exe user32.dll,LockWorkStation")
            break

        if datos.demostracion(rec):
            val=rec.replace(clave,'')
            datos.talk("¡Saludos! Soy Eva, tu asistente virtual personalizada. Estoy aquí para hacer tu vida más sencilla y eficiente. Ya sea que necesites ayuda con tareas, información útil o simplemente una compañía virtual, estaré a tu disposición en todo momento. Mi objetivo es proporcionarte respuestas rápidas y soluciones efectivas. No dudes en preguntarme cualquier cosa. ¡Estoy emocionada de comenzar esta aventura contigo!")
            break
        
        saludo = datos.detectar_saludo(rec)

        if saludo:  
            datos.talk(saludo.capitalize())  # Dice "Buenos días", "Buenas tardes" o "Buenas noches"
            break


    return 0
    

val = 0
datos.show_notification("Bienvenido")
datos.talk("Bienvenido")   
while val == 0:
    val = run()    