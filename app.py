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
  dic = {}
  for file in os.listdir(manualDir + '/' + system + '/'):
    if file.lower().endswith('.pdf'):
      key = file.replace(' ', '').replace('(', '').replace(')', '').replace('.', '').replace('-', '').replace("'", '').lower()
      dic[key] = file

  target = game.replace(' ', '').replace('(', '').replace(')', '').replace('.', '').replace('-', '').replace("'", '').lower() + 'pdf'
  matches = difflib.get_close_matches(target, dic.keys, 1, 0.8)
  if len(matches) > 0 :
    pdfFile = manualDir + '/' + system + '/' + dic[matches[0]]
    subprocess.Popen(["qpdfview", "--quiet", pdfFile])
    return 'Found: ' + pdfFile
  else:
    return 'Not Found: ' + manualDir + '/' + system + '/' + target

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')