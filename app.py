from flask import Flask, render_template, request
import json
from controller import ChangeInput

app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/changeInput', methods=['POST'])
def submit():
    data = request.json
    ChangeInput(data['inp'])
    return 'Form submitted successfully!'

if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)
        app.run(host=config['ip'], port=config['port'], debug=True, threaded=False)