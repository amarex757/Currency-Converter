from flask import Flask, request, render_template
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '[@xQTY+CVRp=.*6329579!&$]'
url = 'https://api.exchangerate.host/latest'

@app.route('/')
def home_page():
      # displays homepage for currency converter
      return render_template('home.html')
