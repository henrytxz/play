from flask import Flask, render_template

app = Flask(__name__)


@app.route('/compare')
def compare():
	return render_template('new_compare.html')


# @app.route('/new', methods=['GET', 'POST'])
# def new():
# 	if request.method == 'POST':
# 		if not request.form['name'] or not request.form['city'] or not request.form['addr']:
# 			flash('Please enter all the fields', 'error')
# 		else:
# 			student = students(request.form['name'],
# 			                   request.form['city'],
# 			                   request.form['addr'],
# 			                   request.form['pin'])
#
# 			db.session.add(student)
# 			db.session.commit()
# 			flash('Record was successfully added')
# 			return redirect(url_for('show_all'))
# 	return render_template('new.html')


if __name__ == '__main__':
	app.run(debug=True)
