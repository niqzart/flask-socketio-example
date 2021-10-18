from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=('https://localhost', 'http://localhost'))


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on("message")
def handle_message(data):
    emit("new_message", data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True, port=5004)
