from distutils.log import debug
from flask import Flask
import subprocess
import sys

app = Flask(__name__)

manualDir = sys.argv[1]

@app.route('/<system>/<game>/manual', methods = ['GET'])
def manual(system=None, game=None):
  subprocess.run(["wmctrl", "-c", "qpdfview"])
  result = subprocess.run(["qpdfview", "--quiet", manualDir + '/' + system + '/' + '/' + game + '.pdf'], capture_output=True)
  return 'Hello ' + system + ',' + game

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')