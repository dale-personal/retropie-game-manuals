from distutils.log import debug
from flask import Flask
import subprocess
import sys

app = Flask(__name__)

manualDir = sys.argv[1]

@app.route('/<system>/<game>/manual', methods = ['GET'])
def manual(system=None, game=None):
  subprocess.run(["wmctrl", "-c", "qpdfview"])
  pdfFile = manualDir + '/' + system + '/' + '/' + game + '.pdf'
  result = subprocess.run([sys.executable, "qpdfview", "--quiet", pdfFile], capture_output=True)
  return pdfFile + ', returnCode=' + str(result.returncode)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')