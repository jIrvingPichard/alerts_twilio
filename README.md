# alerts_twilio

Para que el proyecto se pueda ejecutar correctamente se necesita activar el entorno virtual con el siguiente comando.

python3 -m venv venv

. ./venv/bin/activate


Por si ejecutas el webhook desde ngrok:

ngrok http 5000

Para instalar las librerias del entorno:

Empaquetar:
pip3 freeze > requirements.txt

Instalar:
pip3 install -r requirements.txt
