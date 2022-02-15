from flask import Flask, render_template, request, session, redirect
import json
import os
import math
from werkzeug.utils import secure_filename
from flask_mail import Mail
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


with open("config.json",'r') as c:
    params=json.load(c)["params"]
local_server=True
app = Flask(__name__)
app.secret_key='super-secret-key'
app.config['UPLOAD_FOLDER']=params['upload_location']

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT= '465',
    MAIL_USE_SSL= True,
    MAIL_USERNAME= params['gmail-username'],
    MAIL_PASSWORD= params['gmail-passwd']

)
mail=Mail(app)
if(local_server==True):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)



class Contacts(db.Model):
    #sno, name, phoneno, message, email
    sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80),  nullable=False)
    Phone_No = db.Column(db.String(12), nullable=False)
    Message = db.Column(db.String(120), nullable=False)
    Email = db.Column(db.String(20),  nullable=False)

class Posts(db.Model):
    #sno, name, phoneno, message, email
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12),  nullable=False)
    img_file = db.Column(db.String(12), nullable=False)

@app.route("/")
def origins():
    posts = Posts.query.filter_by().all()
    last=math.ceil(len(posts)/params['no_post'])
    page=request.args.get('page')
    if(not str(page).isnumeric()):
        page=1
    page=int(page)
    #Pagination
    #First
    posts=posts[(page-1)*int(params['no_post']): (page-1)*int(params['no_post'])+int(params['no_post'])]
    if (page==1):
        prev="#"
        next="/?page="+ str(page +1)
    elif (page==last):

        prev="/?page="+ str(page-1)
        next= "#"

    else:
        prev="/?page="+ str(page-1)
        next="/?page="+ str(page+1)



    return render_template('index.html',params=params,posts=posts, prev=prev, next=next)

@app.route("/home")
def origin():
    posts=Posts.query.filter_by().all()
    return render_template('index.html',params=params,posts=posts)



@app.route("/dashboard", methods=['GET','POST'])
def dashboard():

    if('user' in session and session['user']==params['admin_username'] ):
        posts=Posts.query.all()
        return render_template('dashboard.html', params=params, post=posts)

    if request.method=='POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')

        if(username==params['admin_username'] and userpass==params['admin_password']):
            #set the session variable
            session['user']=username
            posts=Posts.query.all()
            return render_template('dashboard.html',params=params, post=posts)
    else:
        return render_template('login.html',params=params)

@app.route("/edit/<string:sno>", methods=['GET','POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_username']): #to check whether user is logged in
        if request.method=='POST':
            box_title=request.form.get('title')
            tline=request.form.get('tline')
            slug=request.form.get('slug')
            content=request.form.get('content')
            img_file=request.form.get('img_file')
            date=datetime.now()

            if sno=='0':
                post=Posts(title=box_title,slug=slug,content=content,img_file=img_file,tagline=tline,date=date)

                db.session.add(post)
                db.session.commit()

            else:
                post=Posts.query.filter_by(sno=sno).first()
                post.title=box_title
                post.slug=slug
                post.content=content
                post.img_file=img_file
                post.tagline=tline

                db.session.commit()

                return redirect('/edit'+sno)
        post=Posts.query.filter_by(sno=sno).first()

        return render_template('edit.html',params=params,sno=sno,post=post)

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/delete/<string:sno>",methods=['GET','POST'])
def delete(sno):
    if ('user' in session and session ['user']==params['admin_username']):
        post=Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()

    return redirect('/dashboard')
@app.route("/uploader", methods=['GET','POST'])
def uploader():
    if (request.method=='POST'):
        f=request.files['file1']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
        return "Uploaded Successfully"

@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post=Posts.query.filter_by(slug=post_slug).first()


    return render_template('post.html',params=params,post=post)

@app.route("/about")
def about():

    return render_template('about.html',params=params)

@app.route("/contact",methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        phone = request.form.get('phone')
        message = request.form.get('message')
        email = request.form.get('email')

        entry=Contacts(Name=name,Phone_No=phone, Message=message,Email=email)

        db.session.add(entry)
        db.session.commit()
        mail.send_message('New Message From'+name,sender='email',
                          recipients=[params['gmail-username']],
                          body=message+"\n"+str(phone))


    return render_template('contact.html',params=params)



app.run(debug=True)  #To allow continous changes while the site is running