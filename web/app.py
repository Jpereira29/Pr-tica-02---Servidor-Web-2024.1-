from flask import Flask, request, render_template

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def process_data():
  data = request.form['data']
  return f'Os dados enviados foram: {data}'

@app.route('/receive', methods=['GET'])
def receive_data():
  data = request.args.get('data')
  return f'Os dados enviados via GET são: {data}'

@app.route('/numeros/<int:num1>/<int:num2>', methods=['GET'])
def soma_numerosget(num1, num2):
  return f'A soma dos números é: {int(num1) + int(num2)}'

@app.route('/numerospost', methods=['GET'])
def soma_numerospost():
  return render_template('numeros.html')

@app.route('/numerospost', methods=['POST'])
def soma_numerospost_calculo():
  num1 = request.form['num1']
  num2 = request.form['num2']
  return f'A soma dos números é: {int(num1) + int(num2)}'

if __name__ == '__main__':
  app.run()
