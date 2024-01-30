import socket
from flask import Flask, request
import subprocess

app = Flask(__name__)

seed = 0

@app.route('/', methods=['GET'])
def get_host():
    host = socket.gethostname()
    hostName = socket.gethostbyname(host)
    return hostName

@app.route('/', methods=['POST'])
def sub_process():
    subprocess.Popen(["python3", "stress_cpu.py"])
    host = socket.gethostname()
    hostName = socket.gethostbyname(host)
    return str(hostName)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) 
