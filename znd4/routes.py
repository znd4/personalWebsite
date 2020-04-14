"""
This is where we define URLs (routes)
"""
from flask import render_template
from znd4 import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/resume')
def resume():
    return render_template('resume.html', title='Resume')

@app.route('/blog')
def blog():
    user = {'username': 'Zane'}
    posts = [
        {
            'title': 'Beautiful, Awesome Animals',
            'content': 'A tale of cute, furry doggos.',
        },
        {
            'title': 'Making Games Matter',
            'content': 'How we make a website with real blog posts',
        },
    ]
    return render_template('blog.html', title='Blog', posts=posts)

