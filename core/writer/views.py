from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from core.models import User,Post
from core import app,db 
from core.forms import PostForm

from core.writer import writer

@writer.route('/newpost',methods=['GET','POST'])
@login_required
def new_post():
    if current_user.is_writer == 'No':
        flash('Unauthorized','danger')
        return redirect(url_for('main.index'))
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!','success')
        return redirect(url_for('main.index'))
    return render_template('newpost.html',form=form)

@writer.route('/post/<post_id>',methods=['GET','POST'])
@login_required
def post(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    return render_template('post.html',post=post)

    
@writer.route('/post/<post_id>/delete',methods=['POST','GET'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if current_user != post.author:
        abort(403) 
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.index'))

    
@writer.route('/post/<post_id>/edit', methods=['GET','POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get(post_id)
    if current_user != post.author:
        abort(403)
    form = PostForm()
    if request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    elif form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('newpost.html',post=post,form=form)
    
