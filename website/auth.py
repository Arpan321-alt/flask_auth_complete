from flask import Blueprint,render_template,flash,request,redirect,url_for,request
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user

auth=Blueprint('auth',__name__)

@auth.route('/loginLogout',methods=['GET'])
def login_logout():
    return render_template('login.html',text='logout successfully')

@auth.route('/login1',methods=['GET'])
def login1():
    return render_template('login.html',user=current_user)

@auth.route('/login',methods=['GET','POST'])
def login():
    email=request.form.get('email')
    password=request.form.get('password')

    user=User.query.filter_by(email=email).first()
    if user:
        if user.password==password:
            login_user(user,remember=True)
            return render_template('home.html',text="logged in suceesfully")
           
        else:
            return render_template('login.html',text="password is incorrect")
    else:
        return render_template('login.html',text='email doesnot exist')

@auth.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return  redirect(url_for('auth.login_logout'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    
    return render_template('sign_up.html',user=current_user)
    
@auth.route('/postSignUp',methods=['POST'])
def SignUp():
    print('fjkjf')
    email=request.form.get('email')
    firstname=request.form.get('firstname')
    password1=request.form.get('password1')
    password2=request.form.get('password2')

        
    print('kjfkjf')
    db.create_all()
    new_user=User(email=email,first_name=firstname,password=password1)
    db.session.add(new_user)
    db.session.commit()
    login_user(user,remember=True)
    print('data inserted')
    return redirect(url_for('views.home'))
    