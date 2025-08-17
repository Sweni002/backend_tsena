from flask_socketio import SocketIO

# Forcer async_mode -> "eventlet" (ou "gevent" si tu préfères)
socketio = SocketIO(cors_allowed_origins="*", async_mode="eventlet")

def init_socketio(app):
    socketio.init_app(app)

    # Exemple d’événement côté serveur
    @socketio.on("connect")
    def handle_connect():
        print("✅ Un client est connecté au WebSocket")

    @socketio.on("disconnect")
    def handle_disconnect():
        print("❌ Un client s'est déconnecté")

    return socketio
