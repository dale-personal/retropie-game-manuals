from flask import Flask
import subprocess
import sys
import difflib
import os

app = Flask(__name__)

manualDir = sys.argv[1]

@app.route('/<system>/<game>/manual', methods = ['GET'])
def manual(system=None, game=None):
  subprocess.Popen(["wmctrl", "-c", "qpdfview"])
  possibilities = []
  for file in os.listdir(manualDir + '/' + system + '/'):
    if file.lower().endswith('.pdf'):
      possibilities.append(file)

  target = game + '.pdf'
  matches = difflib.get_close_matches(target, possibilities, 1, 0.8)
  if matches.count > 0 :
    pdfFile = manualDir + '/' + system + '/' + matches[0]
    subprocess.Popen(["qpdfview", "--quiet", pdfFile])
    return 'Found: ' + pdfFile
  else:
    return 'Not Found: ' + manualDir + '/' + system + '/' + target

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')