from distutils.log import debug
from flask import Flask
import subprocess
import sys

app = Flask(__name__)

manualDir = sys.argv[1]

@app.route('/<system>/<game>/manual', methods = ['GET'])
def manual(system=None, game=None):
  subprocess.Popen(["wmctrl", "-c", "qpdfview"])
  pdfFile = manualDir + '/' + system + '/' + '/' + game + '.pdf'
  subprocess.Popen(["qpdfview", "--quiet", pdfFile])
  return pdfFile

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')