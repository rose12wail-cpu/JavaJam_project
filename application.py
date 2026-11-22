from flask import Flask, render_template, redirect
from database import db, Job
from flask import Flask, render_template, redirect
from database import db, Job
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
application.config['SECRET_KEY'] = 'secret'

db.init_app(application)

admin = Admin(application)
admin.add_view(ModelView(Job, db.session))

with application.app_context():
    db.create_all()

@application.route('/')
def home():
    return render_template('home.html')

@application.route('/jobs')
def jobs():
    open_jobs = Job.query.filter_by(status='Open').all()
    return render_template('jobs.html', jobs=open_jobs)

if __name__ == '__main__':
    application.run(debug=True)