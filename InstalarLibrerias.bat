@echo off
python -m pip install SpeechRecognition
python -m pip install --upgrade google-assistant-sdk[samples]
python -m pip install --upgrade google-auth-oauthlib[tool]
pause
echo Ahora entra en esta web: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio y selecciona la version de python que uses ejemplo: para python 3.8.5 selecciona la que ponga cp38. Tambien tienes que seleccionar la version compatible con tu sistema según los bits que tenga tu procesador, para saberlos escribe python en el cmd ejemplo:
echo ....
echo C :\Users\tu-usuario>python
echo Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit -AQUI ESTAN LOS BITS EN MI CASO 32-(Intel)] on win32
echo Type "help", "copyright", "credits" or "license" for more information.
echo ....
echo Una vez sepas tus BITS y tu version de PYTHON instalada selecciona el archivo que más te convenga, ejemplo: Si tienes 32 bits y python 3.8.5 usa: PyAudio‑0.2.11‑cp38‑cp38‑win32.whl
set /p ArchivoDescargado=Cómo se llama el archivo que acabas de descargar? Asegurate que tenga la extensión .whl!!! 
pip install %ArchivoDescargado%
pause