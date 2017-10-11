import pyodbc
import pandas as pd

conn = pyodbc.connect(
    driver='FreeTDS',
    server='lga-db4.pulse.data',
    port=58321,
    uid='sqoopuser',
    pwd='sqoop@207*',
    tds_version='7.3'
)
# cursor = conn.cursor()

query = """
SELECT * FROM Utility.dbo.ComparePage;
"""

query2 = """
SELECT TOP(3) *
FROM (
    SELECT
      CONVERT(date, dt) AS dt,
      CONCAT(store, '-', CASE WHEN db='fact' then CONCAT(db, tbl) ELSE tbl END) AS name,
      SUM(val) AS val
    FROM Utility.dbo.tblStats
	WHERE
	  dt >= DATEADD(dd, 0, DATEDIFF(dd, 0, GETDATE()-30)) AND
	  (
	    (
	      unit='daily-dl8' AND
	      CONCAT(store, '-', tbl) IN (
	        'lga-sql-advDailyStats',
	        'lga-sql-pubDailyStats',
	        'sjc-sql-advDailyStats',
	        'sjc-sql-pubDailyStats',
	        'vertica-rpt',
	        'vertica-widecompact'
	      )
	    ) OR
	    (
	      unit='hourly-dl8' AND
	      CONCAT(store, '-', tbl) IN (
            'lga-hive-logevent',
            'sjc-hive-logevent',
            'lga-sql-KPIHourly',
            'sjc-sql-KPIHourly',
            'vertica-kpihourly'
	      )
	    )
	  )
	GROUP BY
	  CONVERT(date, dt),
	  CONCAT(store, '-', CASE WHEN db='fact' then CONCAT(db, tbl) ELSE tbl END)
) AS s
PIVOT
(
    SUM(val)
    FOR [name] IN (
	    [vertica-rpt],
	    [vertica-widecompact],
	    [lga-sql-advDailyStats],
	    [lga-sql-pubDailyStats],
	    [lga-sql-KPIHourly],
	    [sjc-sql-advDailyStats],
	    [sjc-sql-pubDailyStats],
	    [sjc-sql-KPIHourly],
	    [lga-hive-logevent],
	    [sjc-hive-logevent],
	    [lga-hive-factlogevent],
	    [sjc-hive-factlogevent],
	    [vertica-kpihourly]
    )
) AS pvt
ORDER BY dt DESC;
"""
# cursor.execute(query)

# for row in cursor:
#     print('row = %r' % (row,))

df = pd.read_sql_query(query, conn)
print 'check it out'
