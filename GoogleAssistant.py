# encoding: utf-8
#PARA INSTALAR PYAUDIO, entrar aquí: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio Luego descargarse la verisón para su sistema operativo 32/64 Y ASEGURARSE QUE EN CP PONGA LA VERSION DE PYTHON QUE USES, EJEMPLO: cp38 Y VERSION DE PYTHON 3.8.5. PARA SABER LOS BITS, ESCRIBIR python EN CMD. 
#pip install <ARCHIVO-DESCARGADO>
#pip install playsound
#google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless --client-secrets <client-secrets.json>

#pip install SpeechRecognition
import speech_recognition as sr

import os
proyecto_id = "<id-de-tu-proyecto>"
model_id = "<id-de-tu-dispositivo>"


def reconoce():
    
    r = sr.Recognizer() #Se crea la instancia para reconocer
    with sr.Microphone() as source:
        print("HABLA AHORA!!!!")
        audio = r.listen(source) #Se escucha el audio

    try:
        print("HA RECONOCIDO:  " + r.recognize_google(audio)) #Se imprime lo escuchado
        return r.recognize_google(audio) #Se devuelve el texto reconocido
    except sr.UnknownValueError:
        print("NO HE PODIDO ENTENDER LO QUE HAS DICHO!")
    except sr.RequestError as e:
        print("ERROR; {0}".format(e))



def EmpezarReconocer():


    while True: #Empieza el bucle
        resultado = reconoce() #Se obtiene el resultado por el return r.recognize_google(audio)
        print(resultado)
        
        if resultado == "hola Google": #Se mira si el texto es igual a hola Google
               
           os.system("pushtotalk.py --project-id "+proyecto_id+" --device-model-id "+model_id) #Si se reconoce el texto llama a el programa
            #pushtotalk.py Está editado para que no tenga bucle y funcione sin la necesidad de darle a ningún botón.

        
EmpezarReconocer() #Empieza el bucle
