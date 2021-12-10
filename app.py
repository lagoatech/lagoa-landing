from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/services')
def services():
  return render_template('services.html')

@app.route('/academy')
def academy():
  return render_template('academy.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/faq')
def faq():
  return render_template('faq.html')

@app.route('/blog-home')
def blog_home():
  return render_template('blog-home.html')

@app.route('/blog-post')
def blog_post():
  return render_template('blog-post.html')