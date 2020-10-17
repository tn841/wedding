from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return 'bk000-Wedding 페이지 입니다.'
