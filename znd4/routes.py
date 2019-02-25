from flask import render_template
from znd4 import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Zane'}
    return render_template('index.html', title='Home')

@app.route('/resume')
def resume():
    user = {'username': 'Zane'}
    return render_template('resume.html', title='Resume')

@app.route('/blog')
def blog():
    user = {'username': 'Zane'}
    return render_template('blog.html', title='Blog')
    
