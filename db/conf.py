def pyodbc_connect(datacenter, database=None):
    data = db_connections[datacenter]
    return "DRIVER=FreeTDS;SERVER={db_server};port={port};DATABASE={database};UID={uid};PWD={pwd};TDS_Version=7.3".format(
        db_server=data['server'],
        port=data['port'],
        database=database if database else data['database'],
        uid=data["user"],
        pwd=data["password"],
    )

db_connections = {
    "lga": {
        "server":   "lga-db3.pulse.data",
        "port":     50577,
        "database": "ContextAd",
        "user":     "sqoopuser",
        "password": "sqoop@207*",
        "instancename": "Portal",
    },
    "sjc": {
        "server":   "sjc-db1.pulse.data",
        "port":     53353,
        "database": "ContextAd",
        "user":     "sqoopuser",
        "password": "sqoop@207*",
        "instancename": "DR",
    },
    "utility": {
        "server":   "lga-db4.pulse.data",
        "port":     58321,
        "database": "Utility",
        "user":     "sqoopuser",
        "password": "sqoop@207*",
        "instancename": "Corp",
    },
}

if __name__ == "__main__":
	print pyodbc_connect('utility')