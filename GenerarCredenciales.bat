@echo off
echo 1-Entra en esta p�gina: https://console.actions.google.com/ 2- Selecciona tu proyecto 3- Selecciona la segunda pesta�a en la parte de arriba(Develop) 4- Device registration 5- Registrar modelo 6- Selecciona el nombre de tu dispositivo, marca y en tipo selecciona LIGHT. Dale a registrar modelo 7- Descargar credenciales OAuth 8- En la siguiente pesta�a puedes seleccionar todos los traits.
echo 9- Con el archivo descargado cambiale el nombre a: client-secrets , aseg�rate de que siga con la extensi�n: .json en el final del nombre.
echo 10- Ahora pon este archivo en el mismo directorio o carpeta en el que tengas el programa que acabas de abrir.
pause
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless --client-secrets client-secrets.json
pause