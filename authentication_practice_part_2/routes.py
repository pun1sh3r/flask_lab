from models  import User
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user, logout_user
from app import app, db, login_manager
from flask import request, render_template, flash, redirect,url_for
import flask

@login_manager.user_loader
def load_user(user_id):
    #return User.query.get(int(id))
    return User.query.get(1)


@app.route("/puto")
def hello_world():
    return "hello puto!!"

@app.route("/", methods=['GET', 'POST'])
def index():

    if flask.request.method == 'GET':
        return '''
            <p>Your credentials:
            username: TheCodeLearner
            password: !aehashf0qr324*&#W)*E!
            </p>
                       <form action='/' method='POST'>
                        <input type='text' name='email' id='email' placeholder='email'/>
                        <input type='password' name='password' id='password' placeholder='password'/>
                        <input type='submit' name='submit'/>
                       </form>
                       '''
    email = "TheCodeLearner"
    if flask.request.form['password'] == "!aehashf0qr324*&#W)*E!":
        user = User(email="TheCodeLearner@gmail.com", username="TheCodeLearner",password="!aehashf0qr324*&#W)*E!")
        login_user(user,remember=True)
        return render_template("logged_in.html", current_user=user)

    return login_manager.unauthorized()




@app.route('/home')
@login_required
def home():
    return render_template('logged_in.html')

@login_manager.unauthorized_handler
def unauthorized():
    return "You are not logged in. Click here to get <a href="+ str("/")+">back to Landing Page</a>"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))