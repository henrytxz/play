from flask import Flask
from flask_sqlalchemy_tutorial import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)


class students(db.Model):
	id = db.Column('student_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	city = db.Column(db.String(50))
	addr = db.Column(db.String(200))
	pin = db.Column(db.String(10))

	def __init__(self, name, city, addr,pin):
		self.name = name
		self.city = city
		self.addr = addr
		self.pin = pin


@app.route('/hello/<name>')
def hello_world(name):
	return 'Hello %s!' % name


@app.route('/blog/<int:post_id>')
def show_blog(post_id):
	return 'Blog Number %d' % post_id


@app.route('/rev/<float:rev_no>')
def revision(rev_no):
	return 'Revision Number %f' % rev_no


if __name__ == '__main__':
	# app.run(debug=True)
	db.create_all()
