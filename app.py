from flask import Flask
import subprocess
import sys
import difflib
import os

app = Flask(__name__)

manualDir = sys.argv[1]

@app.route('/<system>/<game>/manual', methods = ['GET'])
def manual(system=None, game=None):

  # Close the pdf viwer (does nothing if not running)
  subprocess.Popen(["wmctrl", "-c", "qpdfview"])

  # All infocom games are in 4 pdfs
  if system == "zmachine":
    subprocess.Popen(["qpdfview", "--unique", "--quiet", manualDir + '/' + system + '/INFOCOM.PDF'])
    subprocess.Popen(["qpdfview", "--unique", "--quiet", manualDir + '/' + system + '/MANUAL.PDF'])
    subprocess.Popen(["qpdfview", "--unique", "--quiet", manualDir + '/' + system + '/MAP.PDF'])
    subprocess.Popen(["qpdfview", "--unique", "--quiet", manualDir + '/' + system + '/HINTS.PDF'])
    return 'Found ZMachine'

  # Build the dictionary of files to find find the best match.
  # A crude normalization of file name is used a key and used to perform the match.
  dic = {}
  for file in os.listdir(manualDir + '/' + system + '/'):
    if file.lower().endswith('.pdf'):
      key = file.replace(' ', '').replace('(', '').replace(')', '').replace('.', '').replace('-', '').replace("'", '').replace('\\', '').replace('/', '').lower()
      dic[key] = file

  # Perform the same crude normalization of the the target to match.
  target = game.replace(' ', '').replace('(', '').replace(')', '').replace('.', '').replace('-', '').replace("'", '').replace('\\', '').replace('/', '').lower() + 'pdf'
  matches = difflib.get_close_matches(target, dic.keys(), 1, 0.8)

  # If a match was found, use it.
  if len(matches) > 0 :
    pdfFile = manualDir + '/' + system + '/' + dic[matches[0]]
    subprocess.Popen(["qpdfview", "--quiet", pdfFile])
    return 'Found: ' + pdfFile
  else:
    return 'Not Found: ' + manualDir + '/' + system + '/' + target

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')