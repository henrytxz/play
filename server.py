import pyodbc

import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

conn = pyodbc.connect(
    driver='FreeTDS',
    server='lga-db4.pulse.data',
    port=58321,
    uid='sqoopuser',
    pwd='sqoop@207*',
    tds_version='7.3'
)

query = """
SELECT * FROM Utility.dbo.ComparePage;
"""


@app.route('/tsv', methods=['GET'])
def tsv():
	df = pd.read_sql_query(query, conn)
	pivoted = pd.pivot_table(df, values='PaidImpressions', index=['Dt'], columns=['TableName'])
	return pivoted.to_csv(sep='\t')


@app.route('/', methods=['GET'])
def compare():
	return render_template('compare.html')
	# return render_template('mine.html')
	# return render_template('find_js.html')

if __name__ == '__main__':
	app.run(debug=True)
