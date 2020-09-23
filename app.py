

from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def theone():
  takenpath = request.form.get('directory')
  print(takenpath)
  fileList = os.listdir(takenpath)
  filesFound = '<br>\n'.join(fileList)
  print("eggplant interview route: / POST executed with: %s"%takenpath)
  return render_template('output.j2', filesfound = filesFound, directory = takenpath)


@app.route('/', methods = ['GET'])
def main():
  print("eggplant interview route: / GET")
  return render_template('input.j2')



if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)


