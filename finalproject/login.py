from flask import current_app, request, render_template, redirect, url_for
from myapp.models import User
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user
from wtforms import Form, TextField, PasswordField, validators


login_manager = LoginManager()
login_manager.setup_app(current_app)


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


class UserLoginForm(Form):
    username = TextField('Username', [validators.Required(), validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Required(), validators.Length(min=6, max=200)])


@current_app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=username.lower()).first()
        if user:
            if login_user(user):
                current_app.logger.debug('Logged in user %s', user.username)
                return redirect(url_for('secret'))
        error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@current_app.route('/logout', methods=['GET'])
@auth.login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@current_app.route('/secret', methods=['GET'])
@auth.login_required
def secret():
    return 'This is a secret page. You are logged in as {}'.format(current_user.username)