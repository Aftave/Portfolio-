from flask import Flask, render_template, request   

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html',nav_name='Home')

app.run(host='0.0.0.0', port=5000, debug=True)