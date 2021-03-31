from flask import Flask, render_template
from flask_socketio import SocketIO
from utils import database

# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ioweashldkaslfja;g4684'
socketio = SocketIO(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('./ChatApp.html')


def messageRecived():
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('recived my event: ' + str(json))
    socketio.emit('my response', json, callback=messageRecived)
    chat = str(json)
    database.create_chat_table()
    database.add_chat(chat)

if __name__ == '__main__':
    socketio.run(app, debug=True)
