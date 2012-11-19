from flask import flash, redirect, render_template, abort
from bitblog import app
from bitblog.database import db_session
from bitblog.models import Post
from bitblog.forms import PostForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new_post():
    form = PostForm()
    return render_template('new_post.html', form=form)

@app.route('/<regex("[A-Za-z0-9_-]"):slug>')
def post_detail(slug):
    post = Post.query.filter_by(slug=slug).first()
    if post is None:
        abort(404)
    return render_template('post_detail.html', post=post)

@app.route('/<regex("[A-Za-z0-9_-]"):slug>/edit')
def post_edit(slug):
    post = Post.query.filter_by(slug=slug).first()
    if post is None:
        abort(404)
    form = PostForm()
    return render_template('post_edit.html', form=form)