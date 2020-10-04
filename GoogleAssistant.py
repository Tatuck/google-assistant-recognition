# encoding: utf-8
#PARA INSTALAR PYAUDIO, entrar aquí: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio Luego descargarse la veri�n para su sistema operativo 32/64 Y ASEGURARSE QUE EN CP PONGA LA VERSION DE PYTHON QUE USES, EJEMPLO: cp38 Y VERSION DE PYTHON 3.8.5. PARA SABER LOS BITS, ESCRIBIR python EN CMD. 
#pip install <ARCHIVO-DESCARGADO>
#INSTALAR POCKETSPHINX, entrar aquí https://www.lfd.uci.edu/~gohlke/pythonlibs/#pocketsphinx Luego descargarse la version para su sistema operativo 32/64 Y ASEGURARSE QUE EN CP PONGA LA VERSION DE PYTHON QUE USES, EJEMPLO: cp38 Y VERSION DE PYTHON 3.8.5. PARA SABER LOS BITS, ESCRIBIR python EN CMD. 
#pip install <ARCHIVO-DESCARGADO>

#"pip install --upgrade google-api-python-client" o "python -m pip install --upgrade google-auth-oauthlib[tool]"
#google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --headless --client-secrets client_secret_client-id.json
#despues recibes un JSON del cual tienes que copiar el token
#curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d @JSONCAMBIABLE.json https://embeddedassistant.googleapis.com/v1alpha2/projects/<ID-PROYECTO>/deviceModels/
#descarga los client secrets
#pip install playsound
#DESCARGA CURL: https://curl.haxx.se/download.html

#googlesamples-assistant-devicetool --project-id assistantparapc register-model --model assistant-para-pc-ordenawin --type LIGHT --trait action.devices.traits.OnOff --manufacturer Windows --product-name Ordenador --description MiDescripcion
#google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless --client-secrets <client-secrets.json>
#googlesamples-assistant-devicetool --project-id assistantparapc register-device --device pecemolon --model assistant-para-pc-ordenawin --nickname uncompa --client-type SERVICE

#pip install SpeechRecognition
import speech_recognition as sr

import os
proyecto_id = "assistantparapc"
model_id = "assistant-para-pc-ordenawin"


def reconoce():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #SPHINX
    
    #try:
    #    return r.recognize_sphinx(audio)
    #except sr.UnknownValueError:
    #    print("No te entend�")
    #except sr.RequestError as e:
    #    print("ERROR; {0}".format(e))
    


def EmpezarReconocer():


    while True:
        resultado = reconoce()
        print(resultado)
        
        if resultado == "hola Google":
           
           
           
           os.system("pushtotalk.py --project-id "+proyecto_id+" --device-model-id "+model_id)


        
EmpezarReconocer()
