from flask import Flask, jsonify
import datetime, socket, os

app = Flask(__name__)
start_time = datetime.datetime.now(datetime.timezone.utc)

@app.route('/')
def index():
    return jsonify({
        "service": "ping-api",
        "version": "1.0.0",
        "status": "ok"
    })

@app.route('/health')
def health():
    uptime = str(datetime.datetime.now(datetime.timezone.utc) - start_time)
    return jsonify({
        "status": "healthy",
        "uptime": uptime,
        "hostname": socket.gethostname(),
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
