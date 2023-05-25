from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """
    Responde a las llamadas entrantes con un mensaje de texto simple.
    
    Si la URL de la solicitud coincide con 'roplaybeta.com.mx', se captura el código de la solicitud y se envía un mensaje correspondiente.
    Si el código de la solicitud no se reconoce o no está presente, se envía un mensaje indicando que se recibió una solicitud con un código desconocido.
    """
    #Obtener el mensaje
    msg = request.form.get('Body')

    #Obtener el código de la solicitud si la URL coincide con 'roplaybeta.com.mx', de lo contrario, None
    request_code = request.status_code if request.url == 'roplaybeta.com.mx' else None

    #Crear respuesta basada en el código de la solicitud
    resp = MessagingResponse()
    
    if request_code == 100:
        
        resp.message("Received request with code 100")
        
    elif request_code == 200:
        
        resp.message("Received request with code 200")
        
    elif request_code == 500:
        
        resp.message("Received request with code 500")
        
    elif request_code == 501:
        
        resp.message("Received request with code 501")
        
    else:
        
        resp.message("Received request with unknown code")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
