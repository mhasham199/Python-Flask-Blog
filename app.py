import pymysql
pymysql.install_as_MySQLdb() # Installing MySQLdb as the default MySQL library for SQLAlchemy

from flask import Flask, render_template, request, session, redirect # Import essential Flask modules
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy for database operations
from werkzeug.utils import secure_filename # Used to securely store file names for uploads
from datetime import datetime # Importing datetime to store timestamps
import os # Used to handle file paths
import math # Used for calculations (like pagination)
import json # Used to load JSON configuration files

# Define if the server is running locally or in production
local_server = True
# Load configuration parameters from a JSON file (e.g., database URIs, admin credentials)
with open("config.json", 'r') as c:
    params = json.load(c)["params"]

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'super-secret-key' # Secret key for managing sessions
app.config['UPLOAD_FOLDER'] = params['upload_location'] # Directory to save uploaded files

# Configure the database URI depending on whether the server is local or in production
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define the Contacts database model (table structure)
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


# Define the Posts database model (table structure)
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

# Home route displaying paginated posts
@app.route('/')
def home():
    posts = Posts.query.filter_by().all() # Retrieve all posts from the database
    last = math.ceil(len(posts) / int(params['no_of_posts'])) # Calculate the total number of pages
    page = request.args.get('page') # Get the current page from the query parameter
    if not str(page).isnumeric(): # If the page is not a valid number, default to the first page
        page = 1
    
    page = int(page)
    # Slice the posts to only display the posts for the current page
    posts = posts[(page-1) * int(params['no_of_posts']): ((page-1) * int(params['no_of_posts'])) + int(params['no_of_posts'])]

    # Generate the pagination links for previous and next pages
    if page == 1:
        prev = "#"
        next = "/?page="+ str(page+1)
    elif page == last:
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)

    # Render the homepage with posts and pagination links
    return render_template("index.html", params = params, posts = posts, prev = prev, next = next)

# About route
@app.route('/about')
def about():
    return render_template('about.html', params = params) # Render the 'About' page

# Dashboard route for admin login and managing posts
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if 'user' in session and session['user'] == params['admin_username']: # If admin is logged in
        posts = Posts.query.all()
        return render_template('dashboard.html', params = params, posts = posts)



    if request.method == "POST":
        # Check for admin credentials
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if username == params['admin_username'] and userpass == params['admin_password']:
            # Set session variable to indicate successful login
            session['user'] = username
            posts = Posts.query.all() # Fetch posts after login
            return render_template('dashboard.html', params = params, posts = posts)
    return render_template('login.html', params = params)

# Edit or create a new post
@app.route('/edit/<string:sno>', methods = ['GET', 'POST'])
def edit(sno):
    if "user" in session and session['user'] == params['admin_username']:
        if request.method == 'POST':
            # Get form data for editing/creating a post
            box_title = request.form.get('title')
            tagline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno == "0": # Create a new post
                post = Posts(Title = box_title, slug = slug, Content = content, tagline = tagline, img_file = img_file, Date = date)
                db.session.add(post)
                db.session.commit()
            else: # Update an existing post
                post = Posts.query.filter_by(Sr_No=sno).first()
                post.Title = box_title
                post.slug = slug
                post.Content = content
                post.tagline = tagline
                post.img_file = img_file
                post.Date = date
                db.session.commit()
                return redirect('/edit/' + sno)
            
    post = Posts.query.filter_by(Sr_No=sno).first() # Fetch the post for editing
    return render_template('edit.html', params = params, post = post, sno = sno)

# File uploader route
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if "user" in session and session['user'] == params['admin_username']: # Check if admin is logged in
        if request.method =='POST':
            # Save the uploaded file to the server
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded successfully"

# Logout route
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

# Delete a post route
@app.route('/delete/<string:sno>', methods = ['GET', 'POST'])
def delete(sno):
    if "user" in session and session['user'] == params['admin_username']: # Check if admin is logged in
        post = Posts.query.filter_by(Sr_No = sno).first() # Fetch the post to be deleted
        db.session.delete(post) # Delete the post
        db.session.commit()
    return redirect('/dashboard')



# Contact form route
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data from the contact form
        name_input = request.form.get('name')
        email_input = request.form.get('email')
        phone_input = request.form.get('phone')
        msg_input = request.form.get('msg')
        # Add a new entry to the Contacts table
        entry = Contacts(name = name_input, email = email_input, phone = phone_input, msg = msg_input)
        db.session.add(entry)
        db.session.commit()
    
    return render_template('contact.html', params = params)

# Post route to display a single post based on the slug
@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):

    # Fetch the post from the database based on the slug
    post = Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html', params = params, post = post)

# Run the Flask app on the local server with debugging enabled
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)