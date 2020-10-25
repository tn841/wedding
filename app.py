from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def index2():
    return render_template('img.html')


    

if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)