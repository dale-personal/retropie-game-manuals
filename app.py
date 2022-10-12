from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/<system>/<game>/manual', methods = ['GET'])
def manual(system=None, game=None):
  result = subprocess.run(["wmctrl", "-c", "qpdfview"], capture_output=True, text=True)
  return 'Hello ' + system + ',' + game + ', stdout=' + result.stdout + ', stderr=' + result.stderr

if __name__ == '__main__':
    app.run(debug=True, port=8000)