from distutils.log import debug
from flask import Flask
import subprocess
import sys

app = Flask(__name__)

manualDir = sys.argv[1]
isDebug = sys.argv[2]
port = sys.argv[3]


@app.route('/<system>/<game>/manual', methods = ['GET'])
def manual(system=None, game=None):
  subprocess.run(["wmctrl", "-c", "qpdfview"])
  subprocess.run(["qpdfview", "--quiet", manualDir + '/' + system + '/' + '/' + game + '.pdf'])
  return 'Hello ' + system + ',' + game

if __name__ == '__main__':
    app.run(debug=isDebug, port=port)