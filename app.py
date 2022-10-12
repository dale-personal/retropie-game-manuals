from flask import Flask

app = Flask()

@app.route('/<system>/<game>/manual', methods = ['GET'])
def manual(system=None, game=None):
  return 'Hello ' + system + ',' + game

if __name__ == '__main__':
    app.run(port=8000)