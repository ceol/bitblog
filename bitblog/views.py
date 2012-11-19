from flask import flash, redirect, render_template, request, url_for, abort
from bitblog import app
from bitblog.database import db_session
from bitblog.models import Post
from bitblog.forms import PostForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new_post():
    return render_template('new_post.html')

@app.route('/<regex("[A-Za-z0-9_-]"):slug>')
def post_detail(slug):
    post = Post.query.filter_by(slug=slug).first()
    if post is None:
        abort(404)
    return render_template('post_detail.html', post=post)