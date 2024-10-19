import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import math
import json

local_server = True
with open("config.json", 'r') as c:
    params = json.load(c)["params"]
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']


if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']

db = SQLAlchemy(app)
class Contacts(db.Model):
    '''
    Sr_No, name, email, phone, msg, date
    '''
    Sr_No = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(20), nullable=True)


class Posts(db.Model):
    '''
    Sr_No, name, email, phone, msg, date
    '''
    Sr_No = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    Content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    Date = db.Column(db.String(20), nullable=True)
    img_file = db.Column(db.String(20), nullable=True)

@app.route('/')
def home():
    posts = Posts.query.filter_by().all()
    # [0:params['no_of_posts']]
    last = math.ceil(len(posts) / int(params['no_of_posts']))
    page = request.args.get('page')
    if not str(page).isnumeric():
        page = 1
    
    page = int(page)
    posts = posts[(page-1) * int(params['no_of_posts']): ((page-1) * int(params['no_of_posts'])) + int(params['no_of_posts'])]


    if page == 1:
        prev = "#"
        next = "/?page="+ str(page+1)
    elif page == last:
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)

    return render_template("index.html", params = params, posts = posts, prev = prev, next = next)

@app.route('/about')
def about():
    return render_template('about.html', params = params)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if 'user' in session and session['user'] == params['admin_username']:
        posts = Posts.query.all()
        return render_template('dashboard.html', params = params, posts = posts)



    if request.method == "POST":
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if username == params['admin_username'] and userpass == params['admin_password']:
            # set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params = params, posts = posts)
    return render_template('login.html', params = params)

@app.route('/edit/<string:sno>', methods = ['GET', 'POST'])
def edit(sno):
    if "user" in session and session['user'] == params['admin_username']:
        if request.method == 'POST':
            box_title = request.form.get('title')
            tagline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno == "0":
                post = Posts(Title = box_title, slug = slug, Content = content, tagline = tagline, img_file = img_file, Date = date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(Sr_No=sno).first()
                post.Title = box_title
                post.slug = slug
                post.Content = content
                post.tagline = tagline
                post.img_file = img_file
                post.Date = date
                db.session.commit()
                return redirect('/edit/' + sno)
            
    post = Posts.query.filter_by(Sr_No=sno).first()
    return render_template('edit.html', params = params, post = post, sno = sno)

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if "user" in session and session['user'] == params['admin_username']:
        if request.method =='POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded successfully"

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route('/delete/<string:sno>', methods = ['GET', 'POST'])
def delete(sno):
    if "user" in session and session['user'] == params['admin_username']:
        post = Posts.query.filter_by(Sr_No = sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')




@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name_input = request.form.get('name')
        email_input = request.form.get('email')
        phone_input = request.form.get('phone')
        msg_input = request.form.get('msg')
        entry = Contacts(name = name_input, email = email_input, phone = phone_input, msg = msg_input)
        db.session.add(entry)
        db.session.commit()
    
    return render_template('contact.html', params = params)

@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):

    # fetch data(post) from database
    post = Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html', params = params, post = post)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)