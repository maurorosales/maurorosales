from flask import Flask, request
from confluent_kafka import Consumer, KafkaError

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_message():
    message = request.get_json()  # Obtén el mensaje enviado al endpoint

    # Aquí puedes procesar el mensaje según tus necesidades
    # Por ejemplo, puedes imprimirlo en la consola:
    print("Mensaje recibido:", message)

    # Puedes agregar aquí la lógica adicional para procesar el mensaje

    return 'Mensaje recibido correctamente', 200

if __name__ == '__main__':
    app.run(debug=True)
